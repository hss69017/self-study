import time
from selenium import webdriver

#로딩시간
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome("./chromedriver", chrome_options = chrome_options)
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/"
browser.get(url)

# 팝업창 짜증나네
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div/div[2]/button[1]').click()

# 가는날 선택 클릭
# browser.find_element(By.LINK_TEXT, "가는 날").click() # link_text는 <a> tag에만 적용됨, 원래는 보이는 글자로 찾을 때 쓴다.
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()

# 이번달 27일, 28일 선택
# browser.find_elements(By.LINK_TEXT, "27")[0].click() # [0] -> 이번달
# browser.find_elements(By.LINK_TEXT, "28")[0].click() # [0] -> 이번달
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[6]/button/b').click()
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[7]/button/b').click()

# 도착지 제주도 선택
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b').click()
arrival_search = browser.find_element(By.CLASS_NAME, "autocomplete_input__1vVkF")
arrival_search.send_keys("제주")
time.sleep(3) # 검색 지연시간 고려
browser.find_element(By.CLASS_NAME, "autocomplete_search_item__2WRSw").click()

# 항공권 검색 클릭
browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div/button').click()

# 검색 로딩시간 고려
try:
    elem = WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]')))
    # 최대 10초를 기다리며, 만약 저 element가 나온다면 바로 return
    print(elem[0].text) # elem 값이 list로 반환되서 [0] 사용
finally:
    pass
    #browser.quit()

# # 첫번째 결과 출력
# elem = browser.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/div[6]/div/div[2]/div[2]')
# print(elem.text)