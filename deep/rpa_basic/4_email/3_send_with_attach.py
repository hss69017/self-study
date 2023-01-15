import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일입니다." # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = EMAIL_ADDRESS # 받는 사람
msg.set_content("다운로드 하세요")

# MIME type: https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types or
# https://developer.mozilla.org/ko/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
# 저기서 못 찾겠으면 기본값: text/plain(텍스트), application/octet-stream(다른 모든 경우)
# msg.add_attachment()
with open("/Users/gunju/Desktop/self study/python/deep/rpa_basic/3_web/myw3schoolsimage.jpg", "rb") as f:
    msg.add_attachment(f.read(), maintype = "image", subtype = "jpg", filename = f.name) # MIME type

with open("/Users/gunju/Desktop/self study/python/deep/rpa_basic/4_email/테스트.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype = "application", subtype = "pdf", filename = f.name)

with open("/Users/gunju/Desktop/self study/python/deep/rpa_basic/4_email/엑셀.xlsx", "rb") as f:
    msg.add_attachment(f.read(), maintype = "application", subtype = "octet-stream", filename = f.name)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)