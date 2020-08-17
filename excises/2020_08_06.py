"""
============================
Author  : XiaoLei.Du
Time    : 2020/8/6 7:19
E-mail  : 506615839@qq.com
File    : 2020_08_06.py
============================
"""
# f=open(file='text.txt',mode='r',encoding='utf8')
# data=f.readlines()
# print(data)
# f.close()

# f=open(file=r'text.txt',mode='w',encoding='utf8')
# f.write('python666')
# f.close()

'''
请将数据读取出来，转换为以下格式
{'data0': '数据aaa', 'data1': '数据bbb', 'data2': '数据ccc', 'data3': '数据ddd'}
'''

# with open(file='text.txt',mode='r',encoding='utf8') as f:
#     res=f.readlines()
#     di={}
#     for i,v in enumerate(res):
#         key='data{}'.format(i)
#         value=v.strip()
#         # print(key,value)
#         di[key]=value
#     print(di)

'''
# 要求一： 请把这些数据读取出来，到并且存到list中，格式如下
[
{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'}, {'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}
]
# 要求二：将上述数据再次进行转换，转换为下面这种字典格式格式
​
{
   'data1':{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'}, 
   'data2':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}, 
   'data3':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},   
   'data4':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
   'data5':{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}
}
'''
with open(file='case.txt', mode='r', encoding='utf8') as f:
    data=f.readlines()
    cases=[]
    for i in data:
        case=i.strip().split(',')
        datas={}
        for i in case:
            res=i.split(':')
            key=res[0]
            value=res[1]
            datas[key]=value
        cases.append(datas)

    datas = {}
    for i,v in enumerate(cases):
        key='data{}'.format(i+1)
        value=v
        datas[key]=value
    print(datas)

