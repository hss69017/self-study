# https://www.whatismybrowser.com/detect/what-is-my-user-agent/ : 내 접속정보 확인

url = "http://nadocoding.tistory.com"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
# user-agent 정보를 header 정보로 주면 html 문서를 제대로 가져옴(웹스크래핑)
# user-agent가 없으면 어떤 홈페이지는 사람이 아니라고 생각하고 차단하는 경우도 있음
# 티스토리는 이거 없어도 잘 가져옴

import requests

res = requests.get(url, headers = headers) # user-agent 정보를 header 정보로 주면 html 문서를 제대로 가져옴(웹스크래핑)
res.raise_for_status()

with open("nadocoding.html", "w", encoding = "utf8") as f:
    f.write(res.text)