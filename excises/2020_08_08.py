"""
============================
Author  : XiaoLei.Du
Time    : 2020/8/8 11:48
E-mail  : 506615839@qq.com
File    : 2020_08_08.py
============================
"""
# class GirlFriend:
#     gender='女'
#
#     def __init__(self,name,face,height,leg):
#         self.name=name
#         self.face=face
#         self.height=height
#         self.leg=leg
#
#     def skill(self):
#         print(self.gender)
#         print('{}去购物'.format(self.name))
#
#     @classmethod
#     def listen_music(cls):
#         print(cls.gender)
#         print('这是一个类方法')
#
# obj=GirlFriend('小美','好看','170','1米')
# obj1=GirlFriend('小丽','美丽','165','1.5米')
# print(obj.gender)
# print(GirlFriend.gender)
# # print(obj.name)
# # print(obj.face)
# # print(obj.height)
# # print(obj.leg)
# obj1.skill()
# GirlFriend.listen_music()

'''
4、封装一个学生类，(自行分辨定义为类属性还是实例属性)
-  属性：身份(学生)，姓名，年龄，性别，英语成绩，数学成绩，语文成绩，
-  方法一：计算总分，方法二：计算三科平均分，方法三：打印学生的个人信息。
'''

class Student:
    id='学生'

    def __init__(self,name,age,sex,english,maths,chinese):
        self.name=name
        self.age=age
        self.sex=sex
        self.english=english
        self.maths=maths
        self.chinese=chinese

    def sum_score(self):
        res=self.chinese+self.maths+self.english
        return res

    def avg_score(self):
        res= (self.chinese+self.maths+self.english)/3
        return res

    def info(self):
        print('姓名：{},年龄：{},性别：{}'.format(self.name,self.age,self.sex))

# data={'name':'xiaohong','age':18,'sex':'女','english':88,'maths':98,'chinese':86}
# student=Student(**data)
# print(student.__dict__)
'''
5、封装一个测试用例类(自行分辨定义为类属性还是实例属性)，
-  属性：用例编号  url地址   请求参数   请求方法    预期结果   实际结果
'''
class TestCase:
    def __init__(self,case_id,url,data,method,expected,result):
        self.case_id=case_id
        self.url=url
        self.data=data
        self.method=method
        self.expected=expected
        self.result=result
import random
class MyClass:
    attr=100
    __attr=200

    def func(self):
        phone=self.random_phone()
        print(phone)
        print('这是一个实例方法')
        # print(MyClass.attr)
        # print(MyClass.__attr)
        print(self.attr)
        print(self.__attr)

    @classmethod
    def cls_func(cls):
        print('这是一个类方法')

    @staticmethod
    def random_phone():
        phone='130'
        for i in range(8):
            phone+=str(random.randint(0,9))
        return phone

# my_class=MyClass()
# my_class.func()
# phone1=MyClass.random_phone()
# print(phone1)

class BasePhone:
    def call_phone(self):
        print('拨打语音电话')

class PhoneV1(BasePhone):
    def dispaly_music(self):
        print('播放音乐')

    def send_msg(self):
        print('发送短信')

class PhoneV2(PhoneV1):

    def call_phone(self):
        print('拨打视频电话')
        print('视频电话后5分钟切换成语音电话')
        # BasePhone.call_phone(self)
        super().call_phone()

    def paly_game(self):
        print('玩游戏')

# v2=PhoneV2()
# v2.call_phone()
# v2.paly_game()
# v2.dispaly_music()
# v2.send_msg()

# class Cases:
#     pass
#
# case=Cases()

# setattr(case,'name','phone666')
# print(case.name)
#
# setattr(Cases,'id','学生')
# print(Cases.id)
# for i in range(1,11):
#     setattr(case,'data{}'.format(i),i)
#
# print(case.__dict__)

# data = {'case_id': 1, 'title': '用例1', 'url': 'www.baudi.com', 'data': '001'}

# for k,v in data.items():
#     setattr(case,k,v)
# print(case.__dict__)
# title=getattr(case,'title')
# print(title)
# delattr(case,'title')
# print(case.__dict__)

'''
请列表中的每个字典遍历出来，每个字典的数据用一个对象来保存，
要求：通过setattr 把字典中数据设为对象的属性和值，字典中的key对应属性名，value为属性值。
最后把所有的对象，放入一个列表中，得到如下如格式的数据：
[用例对象，用例对象，用例对象...]
class CaseData:
    pass
'''

data=[
{'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 2,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'},
{'case_id': 3, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 4,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'},
{'case_id': 4, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},
{'case_id': 5,  'method': 'post', 'url': '/member/login', 'data': '123','actual': '通过', 'excepted': '通过'},
]

class CaseData:
    pass
cases=[]
for i in data:
    # print(i)
    case=CaseData()
    for k,v in i.items():
        print(k,v)
        setattr(case,k,v)
    cases.append(case)
# print(cases)


