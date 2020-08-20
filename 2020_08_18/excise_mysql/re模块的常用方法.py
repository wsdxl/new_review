"""
Author:dxl
Time: 2020/8/20 7:53
File: re模块的常用方法.py
"""
import re
'''
findall:查找所有符合规范的字符串，返回的是一个列表
search:查找第一个符合规范的字符串，返回出来的是一个匹配对象
'''
#----------------findall----------------------
# s='123sdd333df456f123ff567'
# re1=r'\d{3}'
# res=re.findall(re1,s)
# print(res)

#--------search----------------------
# re2=r'123'
# res1=re.search(re2,s)
# print(res1.group())

 # 如果没有找到符合规范数据，返回的就是一个None
# re3 = re.search(r"345",s)
# print(re3)


# # 使用search，按规则查找，提取分组的数据:使用group方法，
# # group不传参数：获取的是匹配到的所有内容
# # group可以通过参数来指定，获取第几个分组中的内容（获取第一个分组，传入参数1，获取第二个分组，传入参数2。。
# r='344aaa123bbb345ccc456ff23'
# re11=r'aaa(\d{3})bbb(\d{3})ccc'
# res3=re.search(re11,r)
# print(res3.group())
# print(res3.group(1))
# print(res3.group(2))

# # -----------match---------------
# s = "a123abc123aaa123bbb888ccc"
#
# # match：开字符串的开头位置进行匹配，找到符合规范的，返回出来的是一个匹配对象
# # 如果开头的位置不符合规范，那么不会往后面去找，直接返回的是None
# res1 = re.match(r"a123abc",s)
# print(res1.group())

#------------sub------------------
s = "a123abc123aaa123bbb888ccc"
"""
第一个参数：待替换的字符串
第二个参数：目标字符串
第三个参数：要进行替换操作的字符串
第四个参数：可以指定最多替换的次数，非必填（默认替换所有符合规范的字符串）

"""
res5 = re.sub(r'123', "666", s)
print(res5)
