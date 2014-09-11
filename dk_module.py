#-*- coding:utf-8 -*-


from email.mime.text import MIMEText
import smtplib
import sys

"""
這是寄信功能的模組
"""
class gmail:
  def __init__(self):
    self.user = ''
    self.pw = ''
    self.content = ''
    self.toaddrs = ''

def setMail(self):
  #寄件人的信箱，通常自己去申請個GMAIL信箱即可
  gmail_user = self.user 
  gmail_pwd = self.pw
  
  #寄件人資訊
  fromaddr = gmail_user
  #收件人列表，格式為list即可
  toaddrs = self.toaddrs


  #這是GMAIL的SMTP伺服器，如果你有找到別的可以用的也可以換掉
  smtpserver = smtplib.SMTP("smtp.gmail.com",587)
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo()

  #登入系統
  smtpserver.login(gmail_user, gmail_pwd)
   
  #設定寄件資訊
  msg = MIMEText(self.content)
  msg['Content-Type' ] = 'text/plain; charset="utf-8"'
  msg['Subject' ] = u'*********-即時預警通知-*********'
  msg['From' ] = fromaddr
  msg['To' ] = toaddrs
     
  smtpserver.sendmail(fromaddr, toaddrs, msg.as_string())
      
  #記得要登出
  smtpserver.quit()


