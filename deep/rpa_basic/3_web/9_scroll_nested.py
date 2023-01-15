from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome("/Users/gunju/Desktop/self study/python/chromedriver", chrome_options = chrome_options)
browser.maximize_window()

browser.get("https://www.w3schools.com/html/")

time.sleep(2)

# 특정 영역 스크롤
elem = browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[62]')

# 방법1: ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform() # elem이 보이는 영역으로 이동하는 동작.perform() / 수행

# 방법2: 좌표 정보 이용
# xy = elem.location_once_scrolled_into_view # elem이 있는 좌표
# print("type:", type(xy))
# print("value:", xy)

elem.click()

time.sleep(2)
browser.quit()