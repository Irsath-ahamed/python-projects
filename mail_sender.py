from email.message import Emailmessage
from pymail import password 
import ssl
import smtplib


mail_sender= 'irzathahamed52@gmail.com'
mail_receiver='irsath0901@gmail.com'
mail_pw= password
subject='test mail'
body= """
    congratulation, its working!!
"""

em = Emailmessage()
em['from']= mail_sender
em['to']= mail_receiver
em['subject']= subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(mail_sender,mail_pw)
    smtp.sendmail(mail_sender,mail_receiver,em.as_string())


