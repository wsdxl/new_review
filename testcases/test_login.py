"""
============================
Author  : XiaoLei.Du
Time    : 2020/8/16 10:00
E-mail  : 506615839@qq.com
File    : test_login.py
============================
"""
import os
import unittest
from common.contains import DATADIR
from login import login_check
from common.readexcel import ReadExcel
from library.ddt import ddt,data

data_path=os.path.join(DATADIR,'cases.xlsx')
@ddt
class TestLogin(unittest.TestCase):
    excel = ReadExcel(data_path, 'login')
    login_data=excel.read_excel()

    @data(*login_data)
    def test_login(self,case):
        # 准备数据
        data=eval(case['data'])
        expected=eval(case['expected'])
        case_id=case['case_id']
        #调用功能函数
        res=login_check(*data)
        #断言
        try:
            self.assertEqual(res, expected)
        except AssertionError as e:
            self.excel.write(row=case_id+1,column=5,value='未通过')
            raise e
        else:
            self.excel.write(row=case_id+1,column=5,value='已通过')

if __name__ == '__main__':
    unittest.main()

