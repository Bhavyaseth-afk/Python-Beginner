import os
import math
import random
import smtplib


digit = "123456789"
otp_len = 5
otp = random.sample(digit , otp_len)
otps= "".join(otp)
print(otps)


s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login("bhavyaseth.23@gmail.com", "wiigkuivndiakvvi")
emailid = input("Enter your email: ")
s.sendmail('bhavyaseth.23@gmail.com', emailid , otps)
print("OTP sent sucessfully")


a = input("Enter Your OTP >>: ")
if a == otps:
    print("Verified")
else:
    print("Please Check your OTP again")

