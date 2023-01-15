from imap_tools import MailBox
from account import *
import smtplib
from email.message import EmailMessage
from openpyxl import Workbook

max_val = 3 # 최대 선정자 수
applicant_list = [] # 지원자 리스트

print("[1. 지원자 메일 조회]")
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder = "INBOX") as mailbox:
    index = 1 # 순번
    for msg in mailbox.fetch('(SENTSINCE 13-JAN-2023)'): # 오늘 날짜로 찾지 않는 이유는 메일서버의 시간이 다를 수도 있기 때문
        if "파이썬 특강 신청합니다." in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            # print("순번: {} 닉네임: {} 전화번호: {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1

print("[2. 선정 / 탈락 메일 발송]")
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    for applicant in applicant_list:
        to_addr = applicant[0].from_ # 보낸 사람들의 메일 주소
        # index = applicant[1]
        # nickname = applicant[2]
        # phone = applicant[3]
        index, nickname, phone = applicant[1:]

        title = None
        content = None

        if index <= max_val:
            title = "파이썬 특강 안내 [선정]"
            content = "{}님 축하드립니다. 특강 대상자로 선정되셨습니다. (선정순번 {}번)".format(nickname, index)
        else:
            title = "파이썬 특강 안내 [탈락]"
            content = "{}님 아쉽게도 탈락입니다. 취소 인원이 발생하는 경우 연락드리겠습니다. (대기순번 {}번)".format(nickname, index - max_val)

        msg = EmailMessage()
        msg["Subject"] = title
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_addr
        msg.set_content(content)
        smtp.send_message(msg)
        print(nickname + "님에게 메일 발송 완료")

print("[3. 선정자 명단 파일 생성]")
wb = Workbook()
ws = wb.active
ws.append(["순번", "닉네임", "전화번호"])

for applicant in applicant_list[:max_val]:
    ws.append(applicant[1:])

wb.save("/Users/gunju/Desktop/self study/python/deep/rpa_project/result.xlsx")

print("모든 작업이 완료되었습니다.")