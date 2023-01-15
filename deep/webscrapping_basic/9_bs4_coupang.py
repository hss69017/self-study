# HTTP method

# GET: 정보를 url에 기재 / https://www.coupang.com/np/search?minPrice=1000&maxPrice=100000&page=1 /
# &: 변수 및 값 구분 / ?: 뒤에 변수와 값 & 변수와 값 & 변수와 값... / 한 번 전송할 떄 데이터 양에 제한이 있어 큰 정보는 전송 불가
# 보안 데이터는 GET X

# POST: 정보를 http body에 기재
# 보안 데이터, file

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
headers = {"accept-language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7","accept-encoding":"gzip, deflate, br","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-fetch-mode":"document","sec-fetch-mode":"navigate", "sec-fetch-site":"none","sec-fetch-user":"?1","upgrade-insecure-requests":"1","User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
# 쿠팡은 막혀서 headers 정보를 따로 만들어서 적어줘야 하는듯?
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")

items = soup.find_all("li", attrs = {"class":re.compile("^search-product")})
# print(items[0].find("div", attrs = {"class":"name"}).get_text())
for item in items:
    # no ad
    ad_badge = item.find("span", attrs = {"class":"ad-badge-text"})
    if ad_badge:
        print("exclude ad")
        continue

    name = item.find("div", attrs = {"class":"name"}).get_text()

    # no HP
    if "HP" in name:
        print("exclue HP")
        continue

    # 평점이 없는 항목이 있어 에러가 나기 때문에
    price = item.find("strong", attrs = {"class":"price-value"})
    if price:
        price = price.get_text()
    else:
        price = "no price"

    # review >= 100 & rate >= 4.5
    rate = item.find("em", attrs = {"class":"rating"})
    if rate:
        rate = rate.get_text()
    else:
        print("exlucde no rate")
        continue
    
    rate_cnt = item.find("span", attrs = {"class":"rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()
        rate_cnt = rate_cnt[1:-1]
    else:
        print("exclude no review")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)