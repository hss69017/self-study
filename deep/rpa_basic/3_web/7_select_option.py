from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome("/Users/gunju/Desktop/self study/python/chromedriver", chrome_options = chrome_options)
browser.maximize_window()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option")

browser.switch_to.frame("iframeResult")

# 4번째 항목 선택
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[4]')
# elem.click()

time.sleep(2)

# 텍스트 값을 통해서 선택하는 방법
# elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[text()="Audi"]')
# elem.click()

# 텍스트 값이 부분일치하는 항목을 통해서 선택하는 방법
# Au를 포함하는 텍스트 값과 일치하는 항목 찾기
elem = browser.find_element(By. XPATH, '//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()

time.sleep(2)

browser.quit()