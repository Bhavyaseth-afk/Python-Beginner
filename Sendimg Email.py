
import smtplib;smtplib.SMTP_SSL().connect(host='smtp.gmail.com', port=587)

import os
import math
import random
import smtplib

gmailaddress = "bhavyaseth.23@gmail.com"
gmailpassword = "wiigkuivndiakvvi"
mailto = "mrkit07rj@gmail.com"
msg = input("What is your message? \n ")
mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
mailServer.starttls()
mailServer.login(gmailaddress , gmailpassword)
mailServer.sendmail(gmailaddress, mailto , msg)
print(" \n Sent!")
mailServer.quit()
