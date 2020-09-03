"""
Author:dxl
Time: 2020/8/16 15:57
File: myconifg.py
"""
import os
from configparser import ConfigParser
from common.contains import CONFDIR

class Conf(ConfigParser):
    def __init__(self,filename,encoding='utf8'):
        super().__init__()
        self.filename=filename
        self.encoding=encoding
        self.read(filename,encoding)

    def write_data(self,section,option,value):
        self.set(section,option,value)
        self.write(open(self.filename,'w',encoding=self.encoding))

# 获取配置文件的路径
conf_path=os.path.join(CONFDIR,'conf.ini')
conf=Conf(conf_path)

if __name__ == '__main__':
    conf=Conf(r'F:\project\new_review\conf\conf.ini')
    # phone=conf.get('login','phone')
    # print(phone)
    conf.write_data('login','url','http://www.baidu.com')

