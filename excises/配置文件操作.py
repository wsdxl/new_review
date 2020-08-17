"""
Author:dxl
Time: 2020/8/16 14:02
File: 配置文件操作.py
"""
from  configparser import ConfigParser
# 创建一个操作文件的解析对象
conf=ConfigParser()
# 读取文件
conf.read(r'conf.ini',encoding='utf8')
# get方法：读取出来的都是字符串
phone=conf.get('login','phone')
print(phone)
# 配置文件的写入
conf.set('login','password','123456')
conf.write(open('conf.ini','w',encoding='utf8'))