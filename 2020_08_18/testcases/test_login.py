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
from library.ddt import ddt,data
from common.readexcel import ReadExcel
from common.contains import DATADIR
from common.myconifg import conf
from common.hander_request import HeadleRequest
from common.mylogger import mylog


# 获取用例数据路径
data_path=os.path.join(DATADIR,'cases.xlsx')

@ddt
class TestLogin(unittest.TestCase):
    excel=ReadExcel(data_path,'login')
    login_data=excel.read_excel()
    http=HeadleRequest()

    @data(*login_data)
    def test_login(self,case):
        # 准备测试数据
        url=conf.get('env','url')+case['url']
        expected=eval(case['expected'])
        data=eval(case['data'])
        row=case['case_id']+1
        method=case['method']
        headers=eval(conf.get('env','headers'))
        # 发送请求
        response=self.http.send(url=url,method=method,json=data,headers=headers)
        res=response.json()
        # 断言
        try:
            self.assertEqual(expected['code'],res['code'])
            self.assertEqual(expected['msg'],res['msg'])
        except AssertionError as e:
            self.excel.write(row=row,column=8,value='未通过')
            mylog.info('用例：{}---->执行未通过'.format(case['title']))
            print('预期结果:{}'.format(expected))
            print('实际结果:{}'.format(res))
            raise e
        else:
            self.excel.write(row=row, column=8, value='通过')
            mylog.info('用例：{}---->执行通过'.format(case['title']))


if __name__ == '__main__':
    unittest.main()

