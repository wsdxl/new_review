"""
============================
Author  : XiaoLei.Du
Time    : 2020/8/4 7:10
E-mail  : 506615839@qq.com
File    : 2020_08_04.py
============================
"""
'''
1、现有字符串    str1 = "PHP is the best programming language in the world! "
      要求一：将给定字符串的PHP替换为Python      
      要求二：替换以后，将字符串以空格为分割点进行分割得到一个列表
'''
str1 = "PHP is the best programming language in the world! "
# str1=str1.replace('PHP','Python')
# print(str1)
# li1=str1.split(' ')
# print(li1)

'''
2、编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周几”
'''
# list1=['一','二','三','四','五','六','日']
# num=int(input('请输入1-7七个数字：'))
# print('今天是周{}'.format(list1[num-1]))

'''
3、现在有一个列表 li2=[1，2，3，4，5]，
     第一步：请通过三行代码将上面的列表，改成这个样子 li2 = [0，1，2，3，66，5，11，22，33]，
     第二步：对li2进行升序排序 （从小到大）
     第三步：对第二步排序后的列表  再进行降序排序（从大到小
'''
# li2=[1,2,3,4,5]
# li2.insert(0,0)
# print(li2)
# li2[4]=66
# print(li2)
# li2.extend([11,22,33])
# print(li2)
# li2.sort()
# print(li2)
# # li2.reverse()
# li2.sort(reverse=True)
# print(li2)

'''
1、li = [1,2,3,4,5,6,7,8,9] 请通过切片得出结果 [3,6,9] 
2、s = 'python java php',通过切片获取: java
'''
# li = [1,2,3,4,5,6,7,8,9]
# li1=li[2::3]
# # print(li1)
# s = 'python java php'
# s1=s[7:11]
# print(s1)

'''
5、定义一个空列表user=[],   分别提示用户输入，姓名，年龄，身高，用户输入完之后，将输入的信息添加的列表中保存，
然后按照一下格式输出：用户的姓名为：xxx,年龄为：xxx,  身高为：xxx  ,请仔细核对（要求：输出的身高要求保留2位小数）
'''
# user=[]
# name=input('请输入姓名：')
# age=int(input('请输入年龄：'))
# hight=int(input('请输入身高：'))
# user.extend([name,age,hight])
# print(user)
# print('用户的姓名为：{},年龄为：{},  身高为：{:.2f}'.format(name,age,hight))

'''
用户输入一个数值，请判断用户输入的是否为偶数？是偶数输出True,不是输出False
'''
# number=int(input('请输入一个数值:'))
# print(number%2==0)

dic2={'aa':11,'bb':22,'cc':22}
# dic2['cc']=33
# print(dic2)
# dic2.update({'dd':44,'ee':55})
# # print(dic2)
# print(str1)
# del str1
# print(str1)
# print(dic2['aa'])
# print(dic2.get('dd'))
# dic3=dic2.keys()
# dic4=dic2.values()
# # print(list(dic3),list(dic4))
# dic5=dic2.items()
# print(dict(list(dic5)))
# di=dict(name='xiaoming',age=18,sex='男')
# print(di)

# set3={66,77,77,99,77,1,1,2,2,2,3,5}
# print(set3)

'''
二、有5道题（通过字典来存储数据）： 某比赛需要获取你的个人信息，设计一个程序， 
 1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据存储起来，
 2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
 3、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式； 
 4、平台为了保护你的隐私，需要你删除你的联系方式；
 5、你为了取得更好的成绩， 你添加了一项自己的擅长技能。
'''
# info={}
# name=input('请输入姓名：')
# sex=input('请输入性别：')
# age=int(input('请输入年龄：'))
# info.update({'name':name,'sex':sex,'age':age})
# print('我的名字{}，今年{}岁，性别{}，喜欢敲代码'.format(info['name'],info['age'],info['sex']))
# height=int(input('请输入身高：'))
# phone=int(input('请输入联系方式：'))
# info['height']=height
# info['phone']=phone
# info.pop('phone')
# # print(info)
# skill=input('请输入你的技能：')
# info['skill']=skill
# print(info)

'''
三、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
 要求一：去除列表中的重复元素，
 要求二：删除 77，88，99这三个元素
'''
# li = [11,22,33,22,22,44,55,77,88,99,11]
# li1=list(set(li))
# li1.sort()
# print(li1)
# li1.pop()
# li1.pop()
# li1.pop()
# print(li1)


'''
四、有下面几个数据 ，
# t1 = ("aa",11)      t2= (''bb'',22)    li1 = [("cc",11)]
# 请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":22,"bb":22}
# '''
# t1 = ("aa",11)
# t2= ("bb",22)
# li1 = [("cc",11)]
#
# li=[t1,li1[0],t2]
# li1=dict(li)
# li1['cc']=22
# print(li1)


# n = 0
# while n < 10:
#     print(n)
#     if n == 5:
#         break
#     n += 1
# else:
#     print('while循环对应的else')
# print('aaa')

# s = "abchgd"
# for i in s:
#     print(i)

# dic = {"aa": 11, "bb": 22, "cc": 33}
# for i,j in dic.items():
#     print
# t=(1,2)
# a,b=t
# print(a)
# print(b)

# a,b=1,2
# print(a,b)


# users=[{'name':'py01','pwd':'123'},{'name':'py02','pwd':'123'},\
#        {'name':'py03','pwd':'123'},{'name':'py04','pwd':'123'}]
#
# for i in users:
#     # print(i)
#     if i['name']=='py03':
#         print('找到py03')
#         break
# else:
#     print('没有py03')

# li=range(5)
# li1=range(1,10)
# li2=range(1,10,3)
# print(list(li))
# print(list(li1))
# print(list(li2))

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

# for i in  range(1,6):
#     # print(i)
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
'''
*
* *
* * *
* * * *
'''
# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()

# 1、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给打九折，
# 如果购买金额大于100元会给打八折。编写一程序，询问购买价格，再打印出折扣和最终价格。
# price=int(input('请输入你购买的金额：'))
# if price >100:
#     print('打八折，你需要支付{}元'.format(price*0.8))
# elif 50<=price<=100:
#     print('打九折，你需要支付{}元'.format(price*0.9))
# elif 0<price<50:
#     print('不打折，你需要支付{}元'.format(price))
# else:
#     print('你的输入有误')

# 2、输入一个 5 位数，判断它个位与万位相同，十位与千位相 同。 根据判断打印出相关信息，
# 相同打印结果：该数据符合规范，不相同打印：该数据不符合规范
# num=input('请输入一个五位数：')
# if num[0]==num[-1] and num[1]==num[-2]:
#     print('该数据符合规范')
# else:
#     print('该数据不符合规范')

#3、利用random函数生成随机整数，从1-9取出来。然后输入一个数字，来猜，如果大于，则 印大于随机数。
# 小了，则打印小于随机数。如果相等，则打印等于随机数
# from random import randint
# ran=randint(1,9)
# n=int(input('请输入一个数字：'))
# if n >ran:
#     print('{}大于随机数{}'.format(n,ran))
# elif n<ran:
#     print('{}小于随机数{}'.format(n,ran))
# elif n==ran:
#     print('{}等于随机数{}'.format(n, ran))
# else:
#     print('你输入的有误')

# #一、输出99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('{} * {} = {:<4}'.format(i,j,(i*j)),end='')
#     print()

# #2、有1 2 3 4 这四个数字，设计程序计算能组成多少个互不相同且无重复数字的3位数？分别是什么？
# counter=0
# for i in range(1,5):
#     for j in range(1,5):
#         for v in range(1,5):
#             if i != j and j != v and v != i:
#                 counter += 1
#                 print('分别是{}'.format(str(i)+str(j)+str(v)))
# print('能组成{}个互不相同且无重复数字的3位数'.format(counter))

# #3、通过函数实现一个计算器，运行程序分别提示用户输入数字1，数字2，然后再提示用户选择 ：
# # 加【1】    减【2】    乘【3】      除【4】，根据不同的选择完成不同的计算
# def add (a,b):
#     return a+b
#
# def sub (a,b):
#     return a-b
#
# def mul (a,b):
#     return a*b
#
# def div (a,b):
#     return a//b
#
# def counter():
#     li=['加','减','乘','除']
#     a=int(input('输入数字1：'))
#     b=int(input('输入数字2：'))
#     print('请选择 加【1】    减【2】    乘【3】      除【4】 ')
#     num=int(input('选择1-4的数字：'))
#     if num==1:
#         print('你选择的是{}法'.format(li[num-1]))
#         return add(a,b)
#
#     elif num==2:
#         print('你选择的是{}法'.format(li[num - 1]))
#         return sub(a, b)
#
#     elif num==3:
#         print('你选择的是{}法'.format(li[num - 1]))
#         return mul(a, b)
#
#     else:
#         print('你选择的是{}法'.format(li[num - 1]))
#         return div(a, b)
#
#
# res=counter()
# print(res)

#4、学习控制流程时，我们讲了一个登录的案例，现在要求大家通过代码实现一个注册的流程，
#1、运行程序，提示用户，输入用户名，输入密码，再次确认密码。
#2、判读用户名有没有被注册过，如果用户名被注册过了，那么打印结果该用户名已经被注册。
#3、用户名没有被注册过，则判断两次输入的密码是否一致，一致的话则注册成功，否则给出对应的提示。


users = [{"name": "py01", "pwd": "123"},
         {"name": "py02", "pwd": "123"},
         {"name": "py03", "pwd": "123"},
         {"name": "py04", "pwd": "123"}]
def register():
    username = input('请输入用户名：')
    password = input('请输入密码：')
    repass = input('请再次确认密码：')
    for user in users:
        if user==username:
            print('该用户名已经被注册')
            break
    else:
        if password != repass:
            print('两次输入的密码不一致')
        else:
            print('注册成功')
            users.append({"name":username,"pwd":password})


register()
