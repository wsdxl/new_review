"""
Author:dxl
Time: 2020/8/16 22:51
File: hander_request.py
"""
import requests

class HeadleRequest:

    def send(self,url,method,params=None,data=None,json=None,headers=None):
        method=method.lower()
        if method=='post':
            return requests.post(url=url,json=json,data=data,headers=headers)
        elif method=='patch':
            return requests.patch(url=url,json=json,data=data,headers=headers)
        elif method=='get':
            return  requests.get(url=url,params=params)

class HeadleSessionRequest:

    def __init__(self):
        self.se=requests.session()

    def send(self, url, method, params=None, data=None, json=None, headers=None):
        method = method.lower()
        if method == 'post':
            return self.se.post(url=url, json=json, data=data, headers=headers)
        elif method == 'patch':
            return self.se.patch(url=url, json=json, data=data, headers=headers)
        elif method == 'get':
            return self.se.get(url=url, params=params)


if __name__ == '__main__':
    login_url = 'http://api.lemonban.com/futureloan/member/login'
    data = {
        'mobile_phone': '13641878150',
        'pwd': '12345678',
    }
    headers = {
        "X-Lemonban-Media-Type": "lemonban.v2",
        "Content-Type": "application/json"
    }
    http=HeadleRequest()
    response=http.send(url=login_url,method='post',json=data,headers=headers)
    res=response.json()
    print(res)