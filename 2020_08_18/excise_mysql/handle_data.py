"""
Author:dxl
Time: 2020/8/20 8:36
File: handle_data.py
"""
import re
from common.myconifg import conf
# data = '{"mobile_phone":"#phone#","pwd":"#pwd#"}'
# # data1 = '{"member_id": #member_id#,"amount":600}'
# if '#phone#' in data:
#     data=data.replace('#phone#',conf.get('test_data','mobile_phone'))
# if '#pwd#' in data:
#     data=data.replace('#pwd#',conf.get('test_data','pwd'))
# print(data)

# ------------使用正则进行替换----方式不通用----------
# data = '{"mobile_phone":"#phone#","pwd":"#pwd#"}'
# r = "#.+?#"

# res2 = re.search(r, data)
# # print(res2.group())
#
# data=data.replace(res2.group(),conf.get('test_data','mobile_phone'))
# # print(data)
# res3=re.search(r,data)
# # print(res3.group())
# data=data.replace(res3.group(),conf.get('test_data','pwd'))
# print(data)

# res1 = re.findall(r,data)
# print(res1)



# data = '{"mobile_phone":"#phone#","pwd":"#pwd#"}'
# r = "#(.+?)#"
# res = re.search(r,data)
# if res:
#     item=res.group()
#     key=res.group(1)
#     print(item)
#     print(key)
#     data=data.replace(item,conf.get('test_data',key))
# # print(data)
# res1=re.search(r,data)
# if res1:
#     item = res1.group()
#     key = res1.group(1)
#     print(item)
#     print(key)
#     data = data.replace(item, conf.get('test_data', key))
# print(data)

class TestCase:
    member_id=''

data = '{"mobile_phone":"#phone#","pwd":"#pwd#"}'
def replace_data(data):
    r = "#(.+?)#"
    while re.search(r,data):
        res=re.search(r,data)
        item=res.group()
        key=res.group(1)
        try:
            data=data.replace(item,conf.get('test_data',key))
        except:
            data=data.replace(item,getattr(TestCase,key))
    return data

data=replace_data(data)
print(data)



