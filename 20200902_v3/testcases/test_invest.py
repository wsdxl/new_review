"""
Author:dxl
Time: 2020/8/29 21:22
File: test_invest.py
"""
import os
import unittest
import jsonpath
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
class TestInvest(unittest.TestCase):
    excel=ReadExcel(data_path,'invest')
    invest_data=excel.read_excel()
    http=HeadleRequest()


    @data(*invest_data)
    def test_invest(self,case):
        # 准备数据
        # 拼接url
        url = conf.get('env', 'url') + case['url']
        # 提取method
        method = case['method']
        # 提取data
        case['data']=handle_data(case['data'])
        data=eval(case['data'])
        if case['interface']!='login':
            sign=HandleSign.generate_sign(getattr(TestData,'token'))
            data.update(sign)
        # 提取expected
        expected=eval(case['expected'])
        # 提取headers
        headers = eval(conf.get('env', 'headers'))
        if case['interface']!='login':
            headers['Authorization']=getattr(TestData,'token_data')

        # 提取row
        row=case['case_id']+1

        # 发送请求
        response=self.http.send(url=url,method=method,json=data,headers=headers)
        res=response.json()

        if case['interface']=='login':
            # 提取member_id
            id=jsonpath.jsonpath(res,'$..id')[0]
            setattr(TestData,'member_id',str(id))
            # 提取token_type
            token_type=jsonpath.jsonpath(res,'$..token_type')[0]
            # 提取token
            token=jsonpath.jsonpath(res,'$..token')[0]
            setattr(TestData,'token',token)
            # 拼接token_data
            token_data=token_type+' '+token
            setattr(TestData,'token_data',token_data)
        elif case['interface']=='add':
            # 提取loan_id
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
            mylog.info('用例：{}---->执行已通过'.format(case['title']))




