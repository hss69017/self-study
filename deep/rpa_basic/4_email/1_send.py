# google-계정-보안-2단계 인증
#               -앱 비밀번호-메일-Mac-생성
# 같은 폴더 내에 account.py 생성
# EMAIL_ADDRESS = "email address"
# EMAIL_PASSWORD = "앱 비밀번호"

import smtplib
from account import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp: # 첫번째 인자는 이메일의 smtp 주소, 2번째 인자는 포트 번호
    smtp.ehlo() # 연결이 잘 수립되는지 확인
    smtp.starttls() # 모든 내용이 암호화되어 전송
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인

    subject = "test mail" # 메일 제목, 한글 x
    body = "mail body" # 메일 본문, 한글 x

    msg = f"Subject: {subject}\n{body}"
    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg) # 발신자, 수신자, 정해진 형식의 메시지
