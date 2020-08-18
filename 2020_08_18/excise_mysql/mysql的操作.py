"""
Author:dxl
Time: 2020/8/18 8:05
File: mysql的操作.py
"""
'''
python操作mysql需要使用pymysql这个模块，

主机：120.78.128.25
port：3306
用户：future
密码：123456

'''
import pymysql
# 第一步、连接到mysql数据库
con=pymysql.connect(host='120.78.128.25',
                    user='future',
                    password='123456',
                    port=3306,
                    charset='utf8')
# 第二步、创建一个游标对象
cur=con.cursor()
# 第三步、执行sql语句
# 1、准备sql语句
# sql="select mobile_phone from futureloan.member where mobile_phone like  '136%' order by reg_time desc limit 20"
# 2、执行sql语句
# count=cur.execute(sql)
# print(count)

# 第四步、提取SQL语句的查找内容
# 提取查找到的所有内容
# fetchall:返回的是一个查询集(元祖的形式，查询到到的每一条数据为这个元祖中的一个元素)
# data=cur.fetchall()
# print(data)
# for i in data:
#     print(i)

# # fatchone：获取查询到的数据中的第一条
# data=cur.fetchone()[0]
# print(data)

# 其他操作：增删改
# 修改语句
# sql="update futureloan.member set reg_name='小帅哥' where mobile_phone='13650109960';"
# cur.execute(sql)
# 执行完增删改的sql语句之后，需要进行commit提交
# con.commit()

# 插入语句
sql="INSERT into futureloan.member (reg_name,pwd,mobile_phone,type,leave_amount,reg_time) \
VALUES('小哥哥','25D55AD283AA400AF464C76D713C07AD','13650109962',1,2000,'2020-08-18 08:03:19')"
cur.execute(sql)
con.commit()