"""
Author:dxl
Time: 2020/8/18 8:55
File: random_phone.py
"""
import random
def random_phone():
    phone='138'
    for i in range(8):
        phone+=str(random.randint(0,9))
    return phone
phone=random_phone()
str1 = '{"mobile_phone":"#phone#","pwd":"12345678","type":1,"reg_name":"34254sdfs"}'
if '#phone#' in str1:
    str2=str1.replace('#phone#',phone)
    print(str2)