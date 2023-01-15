from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome("/Users/gunju/Desktop/self study/python/chromedriver", options = chrome_options)
browser.maximize_window()

browser.get("https://www.w3schools.com/tags/att_input_type_radio.asp")
curr_handle = browser.current_window_handle
print(curr_handle) # 현재 윈도우 핸들 정보 / CDwindow-70B8C62960AD8A6CDB70E3C6659A89D6

# Try it yourself
browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/a').click() # 새로운 창을 띄우기 때문에, handle이 하나 더 생김

handles = browser.window_handles # 모든 핸들 정보
for handle in handles:
    print(handle)
    browser.switch_to.window(handle) # 각 핸들로 이동
    print(browser.title)
    print()

# 새로 이동된 브라우저에서 뭔가 자동화 작업을 수행하다가

# 그 브라우저 종료
print("현재 핸들 닫기")
browser.close()

# 이전 핸들로 돌아오기
print("처음 핸들로 돌아오기")
browser.switch_to.window(curr_handle)

print(browser.title)

# 브라우저 컨트롤이 가능한지 확인
time.sleep(2)
browser.get("https://daum.net")

# 왜인지 모르겠는데, browser.get 이후 아무것도 안 하고 바로 browser.quit()을 하면 안 먹히네??
test = browser.find_element(By.ID, "o")

time.sleep(2)
browser.quit()