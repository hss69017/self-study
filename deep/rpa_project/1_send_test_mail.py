import smtplib
from account import *
from email.message import EmailMessage
from random import *

nicknames = ["유재석", "박명수", "정형돈", "노홍철", "조세호"]

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for nickname in nicknames:
        msg = EmailMessage()
        msg["subject"] = "파이썬 특강 신청합니다."
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS

        content = nickname + "/" + str(randint(1000, 9999))
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname + "님이 GJ 계정으로 메일 발송 완료")