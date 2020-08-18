"""
Author:dxl
Time: 2020/8/18 22:02
File: test_recharge.py
"""
import unittest
import os
import jsonpath
from common.myconifg import conf
from common.hander_request import HeadleRequest
from library.ddt import ddt,data
from common.readexcel import ReadExcel
from common.contains import DATADIR
from common.mylogger import mylog

data_path=os.path.join(DATADIR,'cases.xlsx')
@ddt
class TestRecharge(unittest.TestCase):
    http=HeadleRequest()
    excel=ReadExcel(data_path,'recharge')
    recharge_data=excel.read_excel()

    @classmethod
    def setUpClass(cls):
        #拼接url地址
        url=conf.get('env','url')+'/member/login'
        data={
            'mobile_phone':conf.get('test_data','mobile_phone'),
            'pwd':conf.get('test_data','pwd')
        }
        headers=eval(conf.get('env','headers'))

        #发送请求
        response=cls.http.send(url=url,method='post',json=data,headers=headers)
        result=response.json()

        #提取member_id
        cls.member_id=jsonpath.jsonpath(result,'$..id')[0]
        #提取token_type
        token_type=jsonpath.jsonpath(result,'$..token_type')[0]
        #提取token
        token=jsonpath.jsonpath(result,'$..token')[0]
        #拼接token
        cls.token_data=token_type+' '+token


    @data(*recharge_data)
    def test_recharge(self,case):
        # 准备用例数据
        url=conf.get('env','url')+case['url']
        method=case['method']
        expected=eval(case['expected'])
        if '#member_id#' in case['data']:
            case['data']=case['data'].replace('#member_id#',str(self.member_id))
        data=eval(case['data'])
        headers=eval(conf.get('env','headers'))
        headers['Authorization']=self.token_data
        row=case['case_id']+1

        # 发送请求
        response=self.http.send(url=url,method=method,json=data,headers=headers)
        res=response.json()

        #断言
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



if __name__ == '__main__':
    unittest.main()