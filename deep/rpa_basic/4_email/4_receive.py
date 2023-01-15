# pip3 install imap-tools: https://pypi.org/project/imap-tools/

from imap_tools import MailBox
from account import *

mailbox = MailBox("imap.gmail.com", 993)
mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder = "INBOX") # INBOX: 받은편지함

# fetch(): () 안에 아무것도 안 쓰면 모든 메일을 가져옴 / reverse = True: 최근 메일부터 가져옴, 기본값은 False / limit: 최대 메일 개수
for msg in mailbox.fetch(limit = 1, reverse = True): 
    print("제목", msg.subject) 
    print("발신자", msg.from_) # 1@gmail.com
    print("수신자", msg.to) # ('1@gmail.com', ) 이런 형태로 출력
    # print("참조자", msg.cc)
    # print("비밀참조자", msg.bcc)
    print("날짜", msg.date) # 2023-01-14 12:41:01-08:00 / gmt 시간을 의미 / gmt-8은 LA
    print("본문", msg.text)
    print("HTML 메시지", msg.html)
    print("=" * 100)

    # 첨부파일
    for att in msg.attachments:
        print("첨부파일 이름", att.filename)
        print("타입", att.content_type)
        print("크기", att.size)

        # 파일 다운르도
        with open("/Users/gunju/Desktop/self study/python/deep/rpa_basic/4_email/download/download_" + att.filename, "wb") as f:
            f.write(att.payload)
            print("첨부파일 {} 다운로드 완료".format(att.filename))

mailbox.logout()