"""
Author:dxl
Time: 2020/8/17 21:57
File: test_register.py
"""
import random
import unittest
import os
from library.ddt import ddt,data
from common.readexcel import ReadExcel
from common.contains import DATADIR
from common.myconifg import conf
from common.hander_request import HeadleRequest
from common.mylogger import mylog

data_path=os.path.join(DATADIR,'cases.xlsx')
@ddt
class TestRegister(unittest.TestCase):
    excel=ReadExcel(data_path,'register')
    register_data=excel.read_excel()
    http=HeadleRequest()



    @data(*register_data)
    def test_register(self,case):
        #准备用例数据
        # 获取url
        url=conf.get('env','url')+case['url']
        # 请求方法
        method=case['method']
        #判断是否有手机号需要替换
        if '#phone#' in case['data']:
            phone=self.random_phone()
            case['data']=case['data'].replace('#phone#',phone)
        data=eval(case['data'])
        #期望结果
        expected=eval(case['expected'])
        #获取请求头
        headers=eval(conf.get('env','headers'))
        #获取用例id
        row=case['case_id']+1

        #发送请求
        response=self.http.send(url=url,method=method,json=data,headers=headers)
        res=response.json()

        #断言
        try:
            self.assertEqual(expected['code'],res['code'])
            self.assertEqual(expected['msg'],res['msg'])
        except AssertionError as e:
            self.excel.write(row=row,column=8,value='未通过')
            mylog.info('用例:{}---->执行未通过'.format(case['title']))
            print('期望结果：{}'.format(expected))
            print('实际结果：{}'.format(res))
            raise e
        else:
            self.excel.write(row=row, column=8, value='通过')
            mylog.info('用例:{}---->执行通过'.format(case['title']))




    @staticmethod
    def random_phone():
        phone='136'
        for i in range(8):
            phone += str(random.randint(0, 9))
        return phone

if __name__ == '__main__':
    unittest.main()