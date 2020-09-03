"""
Author:dxl
Time: 2020/8/30 15:51
File: send_email.py
"""
import os
import smtplib
from  email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from common.contains import REPORTDIR
from common.myconifg import conf



def send_email(file_path):

    # 1.连接smtp服务器
    smtp=smtplib.SMTP_SSL(host=conf.get('email','host'),port=conf.get('email','port'))
    smtp.login(user=conf.get('email','user'),password=conf.get('email','password'))
    # 2.构建邮件
    msg=MIMEMultipart()
    text_msg=MIMEText(open(file_path,'r',encoding='utf8').read(),'html')
    msg.attach(text_msg)

    file_msg=MIMEApplication(open(file_path,'rb').read())
    file_msg.add_header('content-disposition', 'attachment', filename='python.html')
    msg.attach(file_msg)

    msg['from']=conf.get('email','user_from')
    user_to=['530768572@qq.com','dxl20@163.com']
    user_too=','.join(user_to)
    print(user_too)
    msg['to']=user_too
    msg['subject']=conf.get('email','subject')

    # 3.发送邮件
    smtp.send_message(msg,from_addr=conf.get('email','user_from'),to_addrs=user_too)



if __name__ == '__main__':
    file_path = os.path.join(REPORTDIR, 'report.html')
    send_email(file_path)


