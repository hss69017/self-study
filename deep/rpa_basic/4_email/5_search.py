from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder = "INBOX")
# mailbox.logout()

# 이렇게 작성하면 위와 다르게 mailbox.logout()이 필요없다.
with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder = "INBOX") as mailbox:
    # for msg in mailbox.fetch(limit = 5, reverse = True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch("(UNSEEN)"): # 읽지 않은 메일만 가져오기
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정인이 보낸 메일 최근에서부터 5개 가져오기 / 최근 5개 중에서 찾는 것이 아님
    # for msg in mailbox.fetch("(FROM {})".format(EMAIL_ADDRESS), limit = 5, reverse = True): 
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(TEXT "test")'): # 어떤 글자를 포함하는 메일(제목, 본문 포함) / 작은 따옴표와 큰 따옴표 순서가 바뀌면 에러 발생
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(SUBJECT "test")'): # 어떤 글자를 포함하는 메일 (제목만)
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 위에 방식들은 한글로 찾을 수 없다. 그래서 아래와 같이 우회해서 찾아야 한다.
    # for msg in mailbox.fetch(limit = 5, reverse = True):
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(SENTSINCE 07-Nov-2020)', reverse = True, limit = 5): # 특정 날짜 이후의 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # for msg in mailbox.fetch('(ON 08-Jan-2023)', reverse = True, limit = 5): # 특정 날짜에 온 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # for msg in mailbox.fetch('(ON 08-Jan-2023 SUBJECT "transcript")', reverse = True, limit = 5): # 2가지 이상의 조건을 모두 만족하는 메일
    #     print("[{}] {}".format(msg.from_, msg.subject))
    
    # 2가지 이상의 조건 중 하나라도 만족하는 메일
    for msg in mailbox.fetch('(OR ON 08-Jan-2023 SUBJECT "test")', reverse = True, limit = 5):
        print("[{}] {}".format(msg.from_, msg.subject))

# 날짜 정보 가져올 때 참고
# import time
# print(time.strftime("%d-%b-%Y")) # %a: 요일, %b: 월

# import datetime
# dt = datetime.datetime.strptime("2020-12-30", "%Y-%m-%d")
# print(type(dt))
# print(dt.strftime("%d-%b-%Y"))