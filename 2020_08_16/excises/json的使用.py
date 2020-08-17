"""
Author:dxl
Time: 2020/8/16 18:01
File: json的使用.py
"""
import json
data = {"name":"musen","id":18,"msg":None}

json_data = '{"name":"musen","id":19,"msg":null}'
# print(eval(json_data))

# json.loads:将json字符串转换为python的字典类型，会自动将null转换为None
result=json.loads(json_data)
print(result)
print(type(result))

# json.dumps:将python字典类型的数据转换为json字符串，会自动将None转换为null
result1=json.dumps(data)
print(result1)
print(type(result1))
