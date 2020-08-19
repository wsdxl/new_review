"""
Author:dxl
Time: 2020/8/19 21:36
File: re模块.py
"""
import re
##[] 举例一个字符
# re1='[a,b,c]'
# res=re.findall(re1,'1iugfiSHOIFUOFGIDHFGFD2345a6a78b99cc')
# print(res)
# # \d 表示一个数字
# re2='\d'
# res1=re.findall(re2,'1iugfiSHOIFUOFGIDHFGFD2345a6a78b99cc')
# print(res1)

# # \s：表示一个空白键
# re5 = r"\s"
# res5 = re.findall(re5,"a s d a  9999")
# print(res5)

# re21 = r"abc"
# res21 = re.findall(re21,"5678abc789aaa789cc77abcvvbbb")
# print(res21)

# # 同时定义多个规则
# re22 = r"13566778899|13534563456|14788990000"
# res22 = re.findall(re22,"sas13566778899fgh13534563456jkghj14788990000")
# print(res22)

# # 匹配手机号码：11位
# # {m}:表示匹配一个字符m次
# re23 = r"1[3456789]\d{9}"
# res23 = re.findall(re23,"sas13566778899fgh11534563456jkghj12788990000aaa113588889999")
# print(res23)

# # {m,}:表示匹配一个字符至少m次
# re24 = r"\d{7,}"
# res24 = re.findall(re24,"sas12356fgh1234567jkghj12788990000aaa113588889999")
# print(res24)

# # {m,n}表示匹配一个字符出现m次到n次
# # 贪婪模式：如果给定一个范围，它会尽可能的去匹配更多的
# re25 = r"\d{3,5}"
# res25 = re.findall(re25,"aaaaa123456ghj333yyy77iii88jj909768876")
# print(res25)

# # 关闭贪婪模式：在给定的范围后面加个问号（变成非贪婪模式,尽可能匹配最少的）
# re25 = r"\d{3,5}?"
# res25 = re.findall(re25,"aaaaa123456ghj333yyy77iii88jj909768876")
# print(res25)

# # *：表示前一个字符出现0次以上(包括0次)
# re26 =r"\d*"
# res26 = re.findall(re26,"343aa1112df345g1h6699")
# print(res26)

# # +:表示前一个字符出现1次以上(包括1次)
# re26 =r"\d+"
# res26 = re.findall(re26,"343aa1112df345g1h6699")
# print(res26)

# # ? : 表示0次或者一次
# re27 =r"\d?"
# res27 = re.findall(re27,"343aa1112df345g1h6699")
# print(res27)

# # ^:匹配字符串的开头
# re31=r"^python"
# res31 = re.findall(re31,"python999python")
# print(res31)

# # $:匹配字符串的结尾
# re32=r"python$"
# res32 = re.findall(re32,"python999python")
# print

# # \b:匹配单词的边界
# re33=r"\bpython"
# res33 = re.findall(re33,"python999python")
# print(res33)

# # \B:匹配非单词的边界
# re33=r"\Bpython"
# res33 = re.findall(re33,"python999 python")
# print(res33)

# # ()：匹配分组:在匹配的数据中提取数据
# re34=r"aa(\d{3})bb"
# res34 = re.findall(re34,"gg21111h2222hj333klg444hj555klghjkaa123bbhhjhjjaa345bb")
# print(res34)

# re35=r"aa(\d{2,})bb(\d{2,})cc"
# res35 = re.findall(re35,"aa123bb345cc7890ghjkl78aa22bb33cc")
# print(res35)