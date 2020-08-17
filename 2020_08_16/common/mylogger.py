"""
============================
Author  : XiaoLei.Du
Time    : 2020/8/16 11:12
E-mail  : 506615839@qq.com
File    : mylogger.py
============================
"""
import os
import logging
from common.myconifg import conf
from common.contains import LOGDIR

# 读取配置文件中的数据
level=conf.get('logging','level')
s_level=conf.get('logging','s_level')
f_level=conf.get('logging','f_level')
file_nane=conf.get('logging','file_nane')
# 获取日志文件的路径
log_path=os.path.join(LOGDIR,file_nane)

class MyLog:
    @staticmethod
    def mylogger():
        # 一、创建一个名为test_log的日志收集器
        mylog = logging.getLogger('test_log')
        # 二、设置收集器的等级
        mylog.setLevel(level)
        # 三、添加输出渠道到控制台
        # 1、创建一个输出到控制台的输出渠道
        sh = logging.StreamHandler()
        # 2、设置输出渠道的等级
        sh.setLevel(s_level)
        # 3、将输出渠道绑定到日志收集器
        mylog.addHandler(sh)

        # 四、添加输出渠道到文件
        # 1、创建一个输出到文件的输出渠道
        fh = logging.FileHandler(log_path, encoding='utf8')
        # 2、设置输出渠道的等级
        fh.setLevel(f_level)
        # 3、将输出渠道绑定到日志收集器
        mylog.addHandler(fh)

        # 五、设置日志输出格式
        # 创建日志输出格式
        formatter = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
        # 将日志输出格式绑定到输出渠道上
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)
        return mylog

mylog=MyLog.mylogger()



