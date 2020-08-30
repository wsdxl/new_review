"""
Author:dxl
Time: 2020/8/30 11:01
File: send_report.py
"""
'''
通过邮件发送测试报告，
报告已邮件附件的形式发送
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
# 第一步、连接到smtp服务器
smtp=smtplib.SMTP_SSL(host='smtp.qq.com',port=465)

# 第二步、登录服务器
smtp.login(user='506615839@qq.com',password='auzjmtbpidddbgbf')

# 第三步、准备邮件
# 1、准备内容
from_user='506615839@qq.com'
to_user='dxl20@163.com'
subject='发送测试报告'
content='python接口自动化测试报告'
# 读取报告中的内容
file_content=open('report.html', 'rb').read()

# 2、构造邮件
# 1) 构造一封多组件邮件
msg=MIMEMultipart()
# 2) 往多组件邮件中加入文本
text_msg=MIMEText(content, _subtype='plain', _charset='utf8')
msg.attach(text_msg)
# 3) 往多组件邮件中加入附件
file_msg=MIMEApplication(file_content)
file_msg.add_header('content-disposition', 'attachment', filename='python.html')
msg.attach(file_msg)
# 4) 添加发件人、收件人和邮件主题
msg['from']=from_user
msg['to']=to_user
msg['subject']=subject

# 第四步、发送邮件
smtp.send_message(msg,from_addr=from_user,to_addrs=to_user)