#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from smtplib import SMTP_SSL
import UtilTool.Util.Config as conf

# 配置邮箱账户及收发人信息
mailNmae = conf.Config.getSysValue("MailName")
sender = conf.Config.getSysValue("MailUserName")
host = conf.Config.getSysValue("MailHost")
receivers = ['2786937785@qq.com']
password = conf.Config.getSysValue("MailPassword")

# 构建MIMEMultipart对象，并在其中添加邮件内容信息
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header( mailNmae , 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 发送邮件
try:
     #这里使用SMTP_SSL就是默认使用465端口
    smtp = SMTP_SSL(host)
    smtp.login( sender , password )
    smtp.sendmail(sender, receivers, message.as_string())

except smtplib.SMTPException:
    print ("Error: 无法发送邮件")




