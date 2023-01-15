# pip3 install beautifulsoup4 / search "beautifulsoup" on Google
# pip3 install lxml / python3.11부터는 호환이 안되는듯? 내장되어 있는 html.parser or html5lib를 대신 쓰자

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser") # html.parser을 통해서 text화 한 res(사이트 코드 정보)를 python화한 것
print(soup.title)
# print(soup.title.get_text()) # 표시되는 글자만 뽑음
# print(soup.a) # 처음 나오는 <a> element
# print(soup.a.attrs) # attribute of <a>
# print(soup.a["href"]) # 원하는 attribute

# print(soup.find("span", attrs = {"class":"Ntxt_home"})) # attribute 중 class가 ~인 첫번째 <span> element
# print(soup.find(attrs = {"class":"Ntxt_home"})) # 이렇게만 써도 됨, attribute 중 class가 ~인 첫번째 element

# 이런 식으로 정보 중 원하는 것(<a> element)만 가져올 수도 있음
# rank1 = soup.find("li", attrs = {"class": "rank01"})
# print(rank1.a)

# test = soup.find("li", attrs = {"class":"current"})
# print(test.a.get_text())
# print(test.next_sibling) # 다음 형제 element 간에 개행정보가 있을 수 있기 때문에 아무것도 표시 안될수도 있음
# test2 = test.next_sibling.next_sibling
# test3 = test2.next_sibling.next_sibling
# print(test3.a.get_text())
# test2 = test3.previous_sibling.previous_sibling
# print(test2.a.get_text())
# print(test.parent)
# test2 = test.find_next_sibling("li") # 다음 형제를 찾는데 <li>만 찾음. 따라서 개행정보를 건너뛰게 됨
# print(test2.a.get_text())
# test3 = test2.find_next_sibling("li")
# print(test3.a.get_text())
# test2 = test3.find_previous_sibling("li")
# print(test2.a.get_text())

# print(test.find_next_siblings("li")) # 다음 형제들 모두 가져옴

webtoon = soup.find("a", text = "웹툰 홈") # 표시되는 글자로 찾기
print(webtoon)