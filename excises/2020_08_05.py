"""
============================
Author  : XiaoLei.Du
Time    : 2020/8/5 21:56
E-mail  : 506615839@qq.com
File    : 2020_08_05.py
============================
"""
# def func(*args,**kwargs):
#     print(type(args))
#     print(args)
#     print(type(kwargs))
#     print(kwargs)
#
# func(1,2,3,a=11,b=22,c=33)

# def func1(a,b,c):
#     print('a:', a)
#     print('b:', b)
#     print('c:', c)
# li=[1,2,3]
# di={'a':11,'b':22,'c':33}
#
# # func1(*li)
# func1(**di)

# a=10
# def func():
#     a=100
#     print(a)
# func()

# # eval：识别字符串中的python表达式
# li = "[11,22,33]"
# print(eval(li))
#
# #  zip: 聚合打包
#
# li = ["name", "age", "gender","8888","sadasd"]
# li2 = ["木森", 18, "男"]
# a=zip(li,li2)
# print(a)
# # print(list(a))
# print(dict(a))

# s='bnjmfhbhmj'
# res=enumerate(s)
# print(dict(res))

# res1=[
#     {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
#     {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
#     {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}]
#
# def func2(data):
#     return data['case_id']>3
#
# # res=filter(func2,res1)
# # print(list(res))
# f=lambda x:x['case_id']>3
# resl=filter(f,res1)
# print(list(resl))

'''
现在有以下数据， li1 = ["{'a':11,'b':2}","[11,22,33,44]"]  
需要转换为以下格式： li1 = [{'a':11,'b':2},[11,22,33,44]] 
'''
# def func():
#     li1 = ["{'a':11,'b':2}", "[11,22,33,44]"]
#     li2 = [eval(li1[0]), eval(li1[1])]
#     return (li2)
# print(func())

'''
# 有一组用例数据如下：
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]
# 要求一：把上述数据转换为以下格式
res1 = [
    {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]
# 要求二：把上面转换好的数据中case_id大于3的用例数据获取出来,得到如下结果
res = [
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]
'''

cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]

#
# def func1(cases):
#     cases1 = []
#     title = cases[0]
#     for case in cases[1:]:
#         case1 = dict(zip(title, case))
#         cases1.append(case1)
#     return (cases1)
#
# def func2(cases1):
#     datas = []
#     for i in cases1:
#         if i['case_id'] > 3:
#             datas.append(i)
#     return (datas)
#
# res1=func1(cases)
# print(res1)
# res2=func2(res1)
# print(res2)

