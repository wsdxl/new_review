"""
Author:dxl
Time: 2020/8/18 23:32
File: 数据库校验.py
"""
import decimal
from common.myconifg import conf
from common.handle_db import HandleDb

sql='SELECT leave_amount from futureloan.member where mobile_phone="{}"'
phone=conf.get('test_data','mobile_phone')
db=HandleDb()
amount=db.get_one(sql.format(phone))[0]
print(amount)

s_amount = 100.1
s_amount=decimal.Decimal(str(s_amount))
print(type(s_amount))
print(type(amount))
print(s_amount+amount)

