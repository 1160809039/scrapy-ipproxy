#!/usr/bin/python

# @File : EmailUtils.py
# @Author: 邵泽铭
# @Date : 10/9/18
# @Desc :

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
# import const
import traceback

smtpserver = "smtp.qq.com"
fromAddress = "123456@qq.com"
username = "123456@qq.com"
password = "uuuxxabcdrauhedd" 

class EmailUtils(object):
    @staticmethod
    def sendEmailFull(receiver,param):
        msg = MIMEMultipart('mixed')
        if isinstance(receiver,list):
            msg['To'] = ";".join(receiver)
        else:
            msg['To'] = receiver
        if param.get("subject",0)!=0:
            msg['Subject'] = param.get("subject")
        if param.get("subject",0)!=0:
            msg['From'] = fromAddress
        if param.get("text",0)!=0:
            text = param.get("text")
            text_plain = MIMEText(text, 'plain', 'utf-8')
            msg.attach(text_plain)
        if param.get("image",0)!=0:
            sendimagefile = open(param.get("image"), 'rb').read()
            image = MIMEImage(sendimagefile)
            image.add_header('Content-ID', '<image1>')
            image["Content-Disposition"] = 'attachment; filename="attachimage.png"'
            msg.attach(image)
        if param.get("html", 0) != 0:
            text_html = MIMEText(param.get("html"), 'html', 'utf-8')
            text_html["Content-Disposition"] = 'attachment; filename="attachhtml.html"'
            msg.attach(text_html)
        if param.get("file", 0) != 0:
            sendfile = open(param.get("file"), 'rb').read()
            text_att = MIMEText(sendfile, 'base64', 'utf-8')
            text_att["Content-Type"] = 'application/octet-stream'
            # 以下附件可以重命名成aaa.txt
            # text_att["Content-Disposition"] = 'attachment; filename="aaa.txt"'
            # 另一种实现方式
            text_att.add_header('Content-Disposition', 'attachment', filename='aaa.txt')
            # 以下中文测试不ok
            # text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
            msg.attach(text_att)

        try:
            # 邮件服务器及端口号
            smtp = smtplib.SMTP_SSL(smtpserver, 465)
            smtp.login(username, password)
            smtp.sendmail(fromAddress, receiver, msg.as_string())
            print("发送成功")
        except Exception as e:
            print("发送失败")
        finally:
            smtp.quit()

    @staticmethod
    def sendEmail(receiver,subject,content):
        msg = MIMEMultipart('mixed')
        if isinstance(receiver, list):
            msg['To'] = ";".join(receiver)
        else:
            msg['To'] = receiver
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = fromAddress
        msg['To'] = receiver
        try:
            # 邮件服务器及端口号
            smtp = smtplib.SMTP_SSL(smtpserver, 465)
            smtp.login(username, password)
            smtp.sendmail(fromAddress, receiver, msg.as_string())
            print("发送成功")
        except Exception as e:
            print(bytes.decode(bytes(str(e.__doc__), encoding = "utf8")))
            print("发送失败")
        finally:
            smtp.quit()

