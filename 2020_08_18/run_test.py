"""
============================
Author  : XiaoLei.Du
Time    : 2020/8/16 10:24
E-mail  : 506615839@qq.com
File    : run_test.py
============================
"""
import os
import unittest
from common.contains import CASEDIR,REPORTDIR
from library.HTMLTestRunnerNew import HTMLTestRunner

report_path=os.path.join(REPORTDIR,'report.html')

# 一、创建测试套件
suite=unittest.TestSuite()
# 二、加载测试用例到测试套件中
loader=unittest.TestLoader()
suite.addTest(loader.discover(CASEDIR))

# 三、创建一个测试运行程序启动器
runner=HTMLTestRunner(stream=open(report_path, 'wb'),
                      title='练习unittest',
                      description='练习unittest',
                      tester='dxl')

# 四、使用启动器执行测试套件
runner.run(suite)



