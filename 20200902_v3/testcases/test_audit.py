"""
Author:dxl
Time: 2020/8/27 22:04
File: test_audit.py
"""
import unittest
import os
import jsonpath
from common.myconifg import conf
from common.hander_request import HeadleRequest
from common.handle_data import TestData,handle_data
from library.ddt import ddt,data
from common.contains import DATADIR
from common.readexcel import ReadExcel
from common.mylogger import mylog
from common.handle_db import HandleDb
from common.handle_sign import HandleSign

data_path=os.path.join(DATADIR,'cases.xlsx')

@ddt
class TestAudit(unittest.TestCase):
    http=HeadleRequest()
    excel=ReadExcel(data_path,'audit')
    audit_data=excel.read_excel()
    db=HandleDb()

    @classmethod
    def setUpClass(cls):
        # -----------执行用例之前先进行登录-->
        # 登录地址
        url=conf.get('env','url')+'/member/login'
        # 登录参数
        data = {
            'mobile_phone':conf.get('test_data','admin_phone'),
            'pwd':conf.get('test_data','admin_pwd'),
        }
        # 登录headers
        headers=eval(conf.get('env','headers'))
        # 发送请求
        response=cls.http.send(url=url,method='post',json=data,headers=headers)
        res=response.json()
        # 提取member_id
        id=jsonpath.jsonpath(res,'$..id')[0]
        setattr(TestData,'member_id',str(id))
        # 提取token_type
        token_type=jsonpath.jsonpath(res,'$..token_type')[0]
        # 提取token
        token=jsonpath.jsonpath(res,'$..token')[0]
        setattr(TestData,'token',token)
        token_data=token_type+' '+token
        setattr(TestData,'token_data',token_data)

    def setUp(self) :
        # ---------每个审核的用例执行之前都加一个项目，将项目id保存起来----------
        # 获取url
        url=conf.get('env','url')+'/loan/add'
        data={"member_id": getattr(TestData, "member_id"),
                "title": "借钱实现财富自由",
                "amount": 2000,
                "loan_rate": 12.0,
                "loan_term": 3,
                "loan_date_type": 1,
                "bidding_days": 5}
        sign=HandleSign.generate_sign(getattr(TestData,'token'))
        data.update(sign)


        headers=eval(conf.get('env','headers'))
        headers['Authorization']=getattr(TestData,'token_data')

        response=self.http.send(url=url,method='post',json=data,headers=headers)
        result=response.json()
        # 提取 loan_id
        loan_id=jsonpath.jsonpath(result,'$..id')[0]
        setattr(TestData,'loan_id',str(loan_id))

    @data(*audit_data)
    def test_audit(self,case):
        # 准备数据
        url=conf.get('env','url')+case['url']
        case['data']=handle_data(case['data'])
        data=eval(case['data'])
        sign=HandleSign.generate_sign(getattr(TestData,'token'))
        data.update(sign)
        method=case['method']
        expected=eval(case['expected'])
        headers=eval(conf.get('env','headers'))
        headers['Authorization']=getattr(TestData,'token_data')
        row=case['case_id']+1

        # 发送请求
        response=self.http.send(url=url,method=method,json=data,headers=headers)
        json_res=response.json()

        # 如果审核通过的项目返回ok，说明该项目已审核
        if case['title']=='审核通过' and json_res['msg']=='OK':
            pass_loan_id=getattr(TestData,'loan_id')
            setattr(TestData,'pass_loan_id',pass_loan_id)


        # 断言
        try:
            self.assertEqual(json_res['code'],expected['code'])
            self.assertEqual(json_res['msg'],expected['msg'])
            if case['check_sql']:
                sql=handle_data(case['check_sql'])
                status=self.db.get_one(sql)[0]
                self.assertEqual(status,expected['status'])

        except AssertionError as e:
            self.excel.write(row=row,column=8,value='未通过')
            mylog.info('用例：{}---->执行未通过'.format(case['title']))
            print('预期结果：{}'.format(expected))
            print('实际结果：{}'.format(json_res))

            raise e
        else:
            self.excel.write(row=row,column=8,value='通过')
            mylog.info('用例：{}---->执行通过'.format(case['title']))


    @classmethod
    def tearDownClass(cls):
        cls.db.close()



