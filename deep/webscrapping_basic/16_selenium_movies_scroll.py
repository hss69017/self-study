# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies/?hl=en_ZA&gl=US"
# # 나는 미국에서 접속 중이라 이게 소용없음, 이건 구글이 미국 페이지가 우선이어서 한국에서 코딩 실행 시 영어 페이지로 실행되는 것을 한글 페이지로 반환하기 위해 실행하는 것
# headers = {
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
#     # "Accept-Language":"ko-KR,ko" # 한글 페이지 반환
# }

# res = requests.get(url, headers = headers)
# res.raise_for_status
# soup = BeautifulSoup(res.text, "html.parser")

# movies = soup.find_all("div", attrs = {"class":"ULeU3b neq64b"})
# print(len(movies))

# # with open("./webscrapping_basic/movie.html", "w", encoding = "utf8") as f:
# #     # f.write(res.text)
# #     f.write(soup.prettify()) # html 문서를 예쁘게 출력

# for movie in movies:
#     title = movie.find("div", attrs = {"class":"hP61id"}).get_text()
#     print(title)


# 여기서부터는 스크롤 내릴 때 새로고침되면서 다른 목록들이 나오는 실행 화면을 웹스크래핑 하는 부분, google movie 홈페이지 바뀌어서 난 안됨
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome("/Users/gunju/Desktop/self study/python/chromedriver", chrome_options = chrome_options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies"

browser.get(url)

# 지정한 위치로 스크롤 이동
# browser.execute_script("window.scrollTo(0, 1600)") # 해상도 세로 크기인 1600 위치로 스크롤 이동

# 화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time
interval = 2 # 2초에 한 번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "html.parser")

movies = soup.find_all("div", attrs = {"class":"ULeU3b neq64b"})
# attrs = {"class":["aaaaa", "bbbbb"]} 이런 식으로 쓸 수도 있음

for movie in movies:
    title = movie.find("div", attrs = {"class":"hP61id"})
    if title:
        title = title.get_text()
    else:
        continue

    # 할인 전 가격
    original_price = movie.find("span", attrs = {"class":"SUZt4c P8AFK"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "  <할인되지 않은 영화 제외>")
        continue

    # 할인된 가격
    price = movie.find("span", attrs = {"class":"VfPpfd VixbEe"}).get_text()

    # 링크
    link = movie.find("a", attrs = {"class":"Si6A0c ZD8Cqc"})["href"]

    print(f"title: {title}")
    print(f"original price: {original_price}")
    print(f"discounted price: {price}")
    print("link:", "https://play.google.com" + link)
    print("-" * 120)

browser.quit()