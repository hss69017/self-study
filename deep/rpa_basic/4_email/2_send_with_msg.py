import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다." # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = EMAIL_ADDRESS # 받는 사람

# 여러 명에게 메일을 보낼 때
# 방법 1
# msg["To"] = "1@gmail.com", "2@gmail.com"

# 방법 2
# to_list = ["1@gmail.com", "2@gmail.com"]
# msg["To"] = ", ".join(to_list)

# 참조
# msg["Cc"] = "1@gmail.com" # 위와 같이 여러 명을 참조시킬 수도 있음

# # 비밀참조
# msg["Bcc"] = "1@gmail.com"

msg.set_content("테스트 본문입니다.") # 본문

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)