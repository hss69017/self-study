from selenium import webdriver

# 브라우저 안 띄우고 스크래핑하기
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size = 2560x1600")

browser = webdriver.Chrome("/Users/gunju/Desktop/self study/python/chromedriver", options = options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies"
browser.get(url)

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
browser.get_screenshot_as_file("/Users/gunju/Desktop/self study/python/deep/webscrapping_basic/google_movie.png") # 스크린샷 저장

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