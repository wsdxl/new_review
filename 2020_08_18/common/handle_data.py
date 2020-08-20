"""
Author:dxl
Time: 2020/8/20 22:03
File: handle_data.py
"""
import re
from common.myconifg import conf
class TestData:
    pass


def handle_data(data):
    r=r'#(.+?)#'
    while re.search(r,data):
        res=re.search(r,data)
        item=res.group()
        key=res.group(1)
        try:
            data=data.replace(item,conf.get('test_data',key))

        except:
            data=data.replace(item,getattr(TestData,key))

    return data

if __name__ == '__main__':
    data= '{"mobile_phone":"#phone#","pwd":"#pwd#"}'
    res=handle_data(data)
    print(res)