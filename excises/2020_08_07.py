"""
============================
Author  : XiaoLei.Du
Time    : 2020/8/7 7:53
E-mail  : 506615839@qq.com
File    : 2020_08_07.py
============================
"""
# import os
# dir=os.path.dirname(__file__)
# base_path=os.path.dirname(dir)
# print(base_path)
#
# file_path=os.path.join(base_path,r'new_review\2018_08_07.py')
# print(file_path)
# try:
#     score=int(input('请输入成绩：'))
# except:
#     print('输入的内容不规范，默认给0分')
#     score=0
# else:
#     print('没有异常，执行else')
# finally:
#     print('finally不管是否出现异常，都会执行')
# try:
#     # print(a) # NameError
#     b=int('a') # ValueError
# except NameError as e:
#     a=100
#     print(a)
#     print('捕获到了异常NameError:{}'.format(e))
# except ValueError as e1:
#     b=99
#     print(b)
#     print('捕获到了异常ValueError:{}'.format(e1))


# try:
#     print(a) # NameError
#     b=int('a') # ValueError
# except (NameError,ValueError) as e:
#     a=100
#     b=99
#     print('捕获到了异常{}'.format(e))

# res='889'
# expected='888'
# try:
#     assert res==expected
# except AssertionError as e:
#     print('用例未通过')
#     raise e

# 2、改善上节课的注册程序，打开文件的读取数据的时候，如果文件不存在会报错，请通过try-except来捕获这个错误，进行处理


def register():
    try:
        with open(file='user.txt', mode='r', encoding='utf8') as f:
            data = f.readlines()
            users = eval(data)
    except:
        users = []
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
    # print(users)

    with open(file='user.txt', mode='w', encoding='utf8') as f:
        content=str(users)
        f.write(content)


register()
