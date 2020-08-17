"""
============================
Author  : XiaoLei.Du
Time    : 2020/8/3 22:09
E-mail  : 506615839@qq.com
File    : 2020_08_03.py
============================
"""
s1=' 1abcd234abcd '
res=s1.find('d',4)
# print(res)
res2=s1.count('d')
# print(res2)
res3=s1.replace('abc','ABC',1)
# print(res3)
res4=s1.split('a')
# print(res4)
res5=s1.upper()
# print(res5)
res6=s1.lower()
# print(res6)
res7=s1.strip()
# print(res7)
res8=s1.rstrip()
# print(res8)

# str1='今收到{1},交了学费{1}元，开此收据为凭据'
# s=str1.format('jack',50)
# print(s)
# price=float(input('请输入价格：'))
# s='今天的股票价格是{:.2f}'.format(price)
# print(s)
# s1='今天的股票价格是{:.2%}'.format(price)
# print(s1)

# print('{:<8}******'.format('hello'))
# print('{:>8}******'.format('hello'))
# print('{:^8}******'.format('hello'))
# print('我叫%s,我今年%d岁了,我喜欢小数,如%f'%('小明',18,3.1415926))
# name='xiaoming'
# # # age=18
# # # print(f'我的名字叫{name},我今年{age}岁了')

# li=[1,2,'hello','python',2.5]
# # li1=li[:3]
# # print(li1)
# print(li[2])

# a=input('请输入一个数：')
# b=a[::-1]
# if a==b:
#     print('{}是回文数'.format(a))
# else:
#     print('{}不是回文数'.format(a))

li2=[1,2,3]
li2.append(11)
print(li2)
li2.insert(1,22)
print(li2)
li2.extend([33,44,55,1])
print(li2)
# li2.remove(1)
# print(li2)
# li2.pop(3)
# print(li2)
# li2.clear()
# print(li2)
# del li2
# print(li2)
# li3=li2.index(2)
# print(li3)
# li4=li2.count(1)
# print(li4)
# li2[2]=66
# print(li2)
# li2.sort()
# print(li2)
# li2.reverse()
# print(li2)

li5=[111,22,31,41,5,6,888,8,34,8,12,7,33]
li6=li5
li7=li5.copy()
print(li5 is li6)
print(li5 is li7)
print(id(li5))
print(id(li6))
print(id(li7))
