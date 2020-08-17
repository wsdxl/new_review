"""
Author:dxl
Time: 2020/8/16 15:43
File: 配置文件的封装.py
"""
from configparser import ConfigParser
class Conf(ConfigParser):
    def __init__(self,filename,encoding='utf8'):
        super().__init__()
        self.filename=filename
        self.encoding=encoding
        self.read(self.filename,encoding)

    def write_data(self,section,option,value):
        self.set(section=section,option=option,value=value)
        self.write(open(self.filename,'w',encoding=self.encoding))


