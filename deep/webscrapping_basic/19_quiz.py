import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True

browser = webdriver.Chrome("chromedriver", options = options)

url = "https://realty.daum.net/home/apt/danjis/37482/items?business=da_www&mkt_source=&service_type=%EC%9E%85%EC%A3%BC2%EB%85%84%ED%9B%84"
browser.get(url)

soup = BeautifulSoup(browser.page_source, "html.parser")

houses = soup.find_all("div", attrs = {"class":"css-1dbjc4n r-14lw9ot r-eqz5dr"})

for house_idx, house in enumerate(houses):
    print("=" * 11, "매물 {0}".format(house_idx + 1), "=" * 11)

    info = house.find("div", attrs = {"class":"css-1dbjc4n r-13awgt0 r-eqz5dr r-1777fci"})
    price = info.find("div", attrs = {"class":"css-1563yu1"}).get_text()
    print("거래 가격:", price, "(만원)")

    size_place = house.find("div", attrs = {"class":"css-1dbjc4n r-1habvwh r-18u37iz r-14gqq1x"}).get_text()
    print("면적∙동호수:", size_place, "(공급/전용)")