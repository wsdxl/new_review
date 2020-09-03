"""
Author:dxl
Time: 2020/8/20 22:58
File: test_add.py
"""
import os
import jsonpath
import unittest
from library.ddt import ddt,data
from common.readexcel import ReadExcel
from common.contains import DATADIR
from common.myconifg import conf
from common.handle_data import handle_data,TestData
from common.hander_request import HeadleRequest
from common.mylogger import mylog
from common.handle_sign import HandleSign

data_path=os.path.join(DATADIR,'cases.xlsx')
@ddt
class TestAdd(unittest.TestCase):
    excel=ReadExcel(data_path,'add')
    add_data=excel.read_excel()
    http=HeadleRequest()



    @data(*add_data)
    def test_add(self,case):
        # 准备用例数据
        #拼接url
        url=conf.get('env','url')+case['url']
        #获取数据
        case['data']=handle_data(case['data'])
        data=eval(case['data'])
        if case['interface']!='login':
            sign=HandleSign.generate_sign(getattr(TestData,'token'))
            data.update(sign)
        #获取请求方法
        method=case['method']
        # 获取期望结果
        expected=eval(case['expected'])
        #获取请求头
        headers=eval(conf.get('env','headers'))
        if case['interface'] != 'login':
            headers['Authorization']=getattr(TestData,'token_data')
        # 获取row
        row=case['case_id']+1

        # 发送请求
        response=self.http.send(url=url,method=method,json=data,headers=headers)
        res=response.json()

        if case['interface']=='login':
            id=jsonpath.jsonpath(res,'$..id')[0]
            setattr(TestData,'admin_member_id',str(id))
            token_type=jsonpath.jsonpath(res,'$..token_type')[0]
            token = jsonpath.jsonpath(res, '$..token')[0]
            setattr(TestData,'token',token)
            token_data=token_type+' '+token
            setattr(TestData,'token_data',token_data)

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

