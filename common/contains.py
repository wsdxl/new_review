"""
Author:dxl
Time: 2020/8/16 16:22
File: contains.py
"""
import os

# 项目目录的路径 | 如果运行的时候项目目录路径出错，使用上面abspath的方式来获取当前文件的绝对路径
BASEDIR=os.path.dirname(os.path.dirname(__file__))

# 配置文件目录路径
CONFDIR=os.path.join(BASEDIR,'conf')

# 测试数据目录路径
DATADIR=os.path.join(BASEDIR,'data')

#日志文件目录路径
LOGDIR=os.path.join(BASEDIR,'logs')

#测试报告目录路径
REPORTDIR=os.path.join(BASEDIR,'report')

# 测试用例目录路径
CASEDIR=os.path.join(BASEDIR,'testcases')



