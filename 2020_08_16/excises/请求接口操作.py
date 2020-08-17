"""
Author:dxl
Time: 2020/8/16 16:54
File: 请求接口操作.py
"""
import jsonpath
import requests
login_url='http://api.lemonban.com/futureloan/member/login'
data={
    'mobile_phone':'13641878150',
    'pwd':'12345678',
}
headers = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Content-Type": "application/json"
}

response=requests.post(url=login_url, json=data, headers=headers)
res=response.json()
print(res)
# id=res['data']['id']
member_id=jsonpath.jsonpath(res,'$..id')[0]
# print(id)
token_type=jsonpath.jsonpath(res,'$..token_type')[0]
token=jsonpath.jsonpath(res,'$..token')[0]
token_data=token_type+' '+token
# print(token_data)

#----------------------充值接口--------------
headers_data = {
    "X-Lemonban-Media-Type": "lemonban.v2",
    "Content-Type": "application/json",
    "Authorization":token_data
}

recharge_url='http://api.lemonban.com/futureloan/member/recharge'

recharge_data={
    'member_id':member_id,
    'amount':20000
}

response=requests.post(url=recharge_url,json=recharge_data,headers=headers_data)
res1=response.json()
print(res1)
