from imap_tools import MailBox
from account import *

applicant_list = [] # 지원자 리스트


with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder = "INBOX") as mailbox:
    index = 1 # 순번
    for msg in mailbox.fetch('(SENTSINCE 13-JAN-2023)'): # 오늘 날짜로 찾지 않는 이유는 메일서버의 시간이 다를 수도 있기 때문
        if "파이썬 특강" in msg.subject:
            nickname, phone = msg.text.strip().split("/")
            print("순번: {} 닉네임: {} 전화번호: {}".format(index, nickname, phone))
            applicant_list.append((msg, index, nickname, phone))
            index += 1

# for applicant in applicant_list:
#     print(applicant)