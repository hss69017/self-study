import requests
from bs4 import BeautifulSoup
import re

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    return soup

def print_news(index, title, link):
    print("{}. {}".format(index + 1, title))
    print("  (링크: {})".format(link))

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?ie=UTF-8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&sm=chr_hty"
    soup = create_soup(url)
    # 어제보다 00℃ 높아요 / 흐림
    cast = soup.find("p", attrs = {"class":"summary"}).get_text()
    # 현재 00℃ (최저 00℃ / 최고 00℃)
    curr_temp = soup.find("div", {"class":"temperature_text"}).get_text().strip() # 현재 온도
    min_temp = soup.find("span", attrs = {"class":"lowest"}).get_text() # 최저 온도
    max_temp = soup.find("span", attrs = {"class":"highest"}).get_text() # 최고 온도
    # 오전 강수확률 00% / 오후 강수확률 00%
    rain_rate = soup.find("span", attrs = {"class":"rainfall"})
    morning_rain_rate = rain_rate.get_text() # 오전 강수확률
    afternoon_rain_rate = rain_rate.parent.parent.next_sibling.next_sibling.find("span", attrs = {"class":"rainfall"}).get_text() # 오후 강수확률

    # 미세먼지 좋음
    # 초미세먼지 좋음
    dust = soup.find("ul", attrs = {"class":"today_chart_list"})
    # attrs = {"class":"a", "id":"b"} 이런 식으로 쓸 수도 있음
    # 내용으로 찾고 싶다면 find("~", attrs = ~, text = "어떤 내용") 이런 식으로 찾아도 됨, 이 때 text는 list([]) 형식으로도 가능함
    pm10 = dust.find_all("li")[0].get_text().strip() # 미세먼지
    pm25 = dust.find_all("li")[1].get_text().strip() # 초미세먼지

    # 출력
    print(cast)
    print("{} ({} / {})".format(curr_temp, min_temp, max_temp))
    print("오전 강수확률 {} / 오후 강수확률 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print(pm10)
    print(pm25)
    print()

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com/main/ranking/popularDay.naver"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs = {"class":"rankingnews_list"}).find_all("li", limit = 3) # li 태그를 3개까지만 찾는다.
    for index, news in enumerate(news_list):
        title = news.div.a.get_text()
        link = news.div.a["href"]
        print_news(index, title, link)
    print()

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs = {"class":"type06_headline"}).find_all("li", limit = 3)
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 # img 태그가 있으면 2번째(index 순서상 1번째) a 태그의 정보를 사용

        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print_news(index, title, link)
    print()

def scrape_english():
    print("[오늘의 영어회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs = {"id":re.compile("^conv_kor_t")})
    print("(영어지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    print()
    print("(한글지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())
    print()

if __name__ == "__main__": # 이 프로젝트를 실행하면 아래 부분이 동작, 다른 파일에 의해 호출되면 이 부분 실행안됨
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news() # 헤드라인 뉴스 정보 가져오기
    scrape_it_news() # IT 뉴스 정보 가져오기
    scrape_english() # 오늘의 영어회화 가져오기