import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies"
# 나는 미국에서 접속 중이라 이게 소용없음, 이건 구글이 미국 페이지가 우선이어서 한국에서 코딩 실행 시 영어 페이지로 실행되는 것을 한글 페이지로 반환하기 위해 실행하는 것
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    # "Accept-Language":"ko-KR,ko" # 한글 페이지 반환
}

res = requests.get(url, headers = headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "html.parser")

movies = soup.find_all("div", attrs = {"class":"ULeU3b neq64b"})
print(len(movies))

# with open("./webscrapping_basic/movie.html", "w", encoding = "utf8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify()) # html 문서를 예쁘게 출력

for movie in movies:
    title = movie.find("div", attrs = {"class":"hP61id"}).get_text()
    print(title)