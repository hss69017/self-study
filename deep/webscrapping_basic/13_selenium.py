# pip3 install selenium
# chrome-점 3개-도움말-버전 확인
# search "chromedriver" on Google & download
# 해당 폴더에 가서 명령어 "xattr -d com.apple.quarantine chromedriver" 입력 / 다른 디렉토리에서 하려면 또 입력해줘야 함

# selenium 공부: https://selenium-python.readthedocs.io/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By # selenium이 상위 버전으로 find_element_by_class_name 함수를 쓰고 싶을 떄
from selenium.webdriver.common.keys import Keys # for 'Keys.Enter'

# 실행 후 크롬 자동꺼짐 방지 옵션
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome("./chromedriver", chrome_options = chrome_options)
# chromedriver path, 실행 후 크롬 자동꺼짐 방지 옵션
# browser.get("https://naver.com")

# # elem = browser.find_element_by_class_name("link_login") # selenium이 상위 버전으로 실행되지 않는 명령어
# elem = browser.find_element(By.CLASS_NAME, "link_login") # 이렇게 써야 함
# elem.click() # elem = naver login button, # 만약 글자를 입력해야 하는 칸에 글자가 있을 경우 지우려면 clear()
# browser.back() # 이전 페이지
# browser.forward() # 페이지 다시 앞으로 돌아가기
# browser.refresh() # refresh
# browser.back()
# elem = browser.find_element(By.ID, "query") # 검색창

# # 커맨드 창에서 elem.send_keys("나도코딩") 실행 시 오류 발생, 해결방법
# # from selenium.common.exceptions import StaleElementReferenceException
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions
# # ignored_exceptions = StaleElementReferenceException
# # elem = WebDriverWait(browser, 1, ignored_exceptions = ignored_exceptions).until(expected_conditions.presence_of_element_located((By.ID, "query")))

# elem.send_keys("나도코딩") # 검색창에 나도코딩 입력
# elem.send_keys(Keys.ENTER) # 엔터키 입력

# elem = browser.find_elements(By.TAG_NAME, "a") # a element 다 가져오기
# for e in elem:
#     e.get_attribute("href")

# browser.get("https://daum.net")
# elem = browser.find_element(By.NAME, "q")
# elem.send_keys("나도코딩")
# elem.send_keys(Keys.ENTER)
# browser.back()
# elem = browser.find_element(By.NAME, "q")
# elem.send_keys("나도코딩")
# elem = browser.find_element(By.XPATH, '//*[@id="daumSearch"]/fieldset/div/div/button[3]')
# elem.click()

# browser.close() # 현재 열려있는 탭 종료
# browser.quit() # 브라우저 종료

# 1. 네이버로 이동
browser.get("https://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME, "link_login")
elem. click()

# 3. id, pw 입력
browser.find_element(By.ID, "id").send_keys("id")
browser.find_element(By.ID, "pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element(By.ID, "log.login").click()

time.sleep(3) # 3초 대기, 이게 없으면 명령어 실행이 크롬 동작보다 빨라 원하는 코딩대로 작동이 안됨

# 5. id를 새로 입력
# browser.find_element(By.ID, "id").send_keys("my_id")
# browser.find_element(By.ID, "id").clear() # 원래 칸에 있는 것을 지우는 것
# browser.find_element(By.ID, "id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source) # 현재 페이지에 있는 모든 html 문서 반환

# 7. 브라우저 종료
browser.quit()