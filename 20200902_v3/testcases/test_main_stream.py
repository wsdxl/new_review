"""
Author:dxl
Time: 2020/8/29 22:27
File: test_main_stream.py
"""
import os
import random
import unittest
import jsonpath
from library.ddt import ddt,data
from common.contains import DATADIR
from common.readexcel import ReadExcel
from common.myconifg import conf
from common.handle_data import TestData,handle_data
from common.hander_request import HeadleRequest
from common.mylogger import mylog
from common.handle_sign import HandleSign

data_path=os.path.join(DATADIR,'cases.xlsx')

@ddt
class TestMainStream(unittest.TestCase):
    excel=ReadExcel(data_path,'main_stream')
    cases=excel.read_excel()
    http=HeadleRequest()

    @data(*cases)
    def test_main_stream(self,case):
        # 准备数据
        # 拼接url
        url=conf.get('env','url')+case['url']
        # 对url中的参数进行替换
        url=handle_data(url)
        # 提取method
        method=case['method']
        if case['title']=='管理员注册':
            admin_phone=self.random_phone()
            setattr(TestData,'admin_phone',admin_phone)
        if case['title']=='用户注册':
            phone=self.random_phone()
            setattr(TestData,'phone',phone)
        case['data']=handle_data(case['data'])
        data=eval(case['data'])
        if case['interface']!='register'and case['interface']!='login' and case['interface']!='loans':
            sign=HandleSign.generate_sign(getattr(TestData,'token'))
            data.update(sign)

        # 提取expected
        expected=eval(case['expected'])
        # 提取 row
        row=case['case_id']+1

        # 提取headers
        headers = eval(conf.get('env', 'headers'))
        if case['interface'] != 'register' and case['interface'] != 'login':
            headers['Authorization'] = getattr(TestData, 'token_data')

        # 发送请求
        response=self.http.send(url=url,method=method,json=data,params=data,headers=headers)
        res=response.json()

        if case['interface']=='login':
            member_id=jsonpath.jsonpath(res,'$..id')[0]
            token_type=jsonpath.jsonpath(res,'$..token_type')[0]
            token=jsonpath.jsonpath(res,'$..token')[0]
            setattr(TestData,'token',token)
            token_data=token_type+' '+token
            setattr(TestData,'member_id',str(member_id))
            setattr(TestData,'token_data',token_data)
        elif case['interface']=='add':
            loan_id=jsonpath.jsonpath(res,'$..id')[0]
            setattr(TestData,'loan_id',str(loan_id))

        # 断言
        try:
            self.assertEqual(expected['code'],res['code'])
            self.assertEqual(expected['msg'],res['msg'])
        except AssertionError as e:
            self.excel.write(row=row,column=8,value='未通过')
            mylog.info('用例：{}---->执行未通过'.format(case['title']))
            print('预期结果：{}'.format(expected))
            print('实际结果：{}'.format(res))
            raise e

        else:
            self.excel.write(row=row, column=8, value='通过')
            mylog.info('用例：{}---->执行通过'.format(case['title']))


    @staticmethod
    def random_phone():
        phone='186'
        for i in range(8):
            phone+=str(random.randint(0,9))
        return phone
