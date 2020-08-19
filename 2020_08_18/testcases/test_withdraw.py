"""
Author:dxl
Time: 2020/8/19 21:50
File: test_withdraw.py
"""
import os
import jsonpath
import unittest
import decimal
from library.ddt import ddt,data
from common.readexcel import ReadExcel
from common.contains import DATADIR
from common.myconifg import conf
from common.hander_request import HeadleRequest
from common.handle_db import HandleDb
from common.mylogger import mylog

data_path=os.path.join(DATADIR,'cases.xlsx')
@ddt
class TestWithdraw(unittest.TestCase):
    excel=ReadExcel(data_path,'withdraw')
    withdraw_data=excel.read_excel()
    http=HeadleRequest()
    db=HandleDb()

    @classmethod
    def setUpClass(cls):
        cls.phone=conf.get('test_data','mobile_phone')
        cls.pwd=conf.get('test_data','pwd')

    @data(*withdraw_data)
    def test_withdraw(self,case):
        # 准备测试数据
        url=conf.get('env','url')+case['url']
        method=case['method']
        expected=eval(case['expected'])
        if '#member_id#' in case['data']:
            case['data']=case['data'].replace('#member_id#',str(self.member_id))
        if '#phone#' in case['data']:
            case['data'] = case['data'].replace('#phone#', self.phone)
        if '#pwd#' in case['data']:
            case['data'] = case['data'].replace('#pwd#', self.pwd)
        data=eval(case['data'])
        row=case['case_id']+1
        headers=eval(conf.get('env','headers'))
        if case['interface']!='login':
            headers['Authorization']=self.token_data
        if case['check_sql']:
            sql=case['check_sql'].format(conf.get('test_data','mobile_phone'))
            before_amount=self.db.get_one(sql)[0]

        # 发送请求
        response=self.http.send(url=url,method=method,json=data,headers=headers)
        result=response.json()

        if case['interface']=='login':
            TestWithdraw.member_id=jsonpath.jsonpath(result,'$..id')[0]
            token=jsonpath.jsonpath(result,'$..token')[0]
            token_type=jsonpath.jsonpath(result,'$..token_type')[0]
            TestWithdraw.token_data=token_type+' '+token


        # 断言
        try:
            self.assertEqual(expected['code'],result['code'])
            self.assertEqual(expected['msg'],result['msg'])
            if case['check_sql']:
                sql=case['check_sql'].format(conf.get('test_data','mobile_phone'))
                after_amount=self.db.get_one(sql)[0]
                amount=decimal.Decimal(str(data['amount']))
                self.assertEqual(before_amount-after_amount,amount)
        except AssertionError as e:
            self.excel.write(row=row,column=8,value='未通过')
            mylog.info('用例：{}---->执行未通过'.format(case['title']))
            print('预期结果：{}'.format(expected))
            print('实际结果：{}'.format(result))
            raise e
        else:
            self.excel.write(row=row,column=8,value='通过')
            mylog.info('用例：{}---->执行通过'.format(case['title']))
