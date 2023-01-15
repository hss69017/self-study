# requests와 selenium 차이
# requests: 웹페이지(html) 읽어오기, 빠르다, 동적 웹페이지 x
# selenium: 웹페이지 자동화, 느리다, 동적 웹페이지 o
# 이후 requests나 selenium으로 가져온 정보를 beautifulsoup으로 웹 스크래핑(원하는 데이터 추출)

# requests는 주어진 url을 통해 받아온 html에 원하는 정보가 있을 때 사용
# selenium은 로그인, 어떤 결과에 대한 필터링 등 사용자가 어떤 동작을 해야 하는 경우 사용, 크롬버전에 맞는 chromedriver 파일이 있어야 함
# 또한 페이지에 대한 로딩 등 시간을 기다려야 할 때가 있음

# 무분별한 웹 크롤링 / 스크래핑은 대상 서버에 부하: 게정, ip 차단 가능
# 데이터 사용 주의: 이미지, 텍스트 등 데이터 무단 활용 금지
# robots.txt: 법적 효력은 없으나, 대상 사이트의 권고임 예) google.com/robots.txt

import requests # pip3 install requests

res = requests.get("https://google.com")
res.raise_for_status() # if there's a problem, it prints an error code and terminates the program.
# print("answer code:", res.status_code) # 200: normal, 403: 페이지 접근 권한 X

# if res.status_code == requests.codes.ok: # or 200
#     print("It's normal.")
# else:
#     print("There's a problem. [error code " + res.status_code + "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding = "utf8") as f:
    f.write(res.text)