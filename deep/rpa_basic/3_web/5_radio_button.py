from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome("/Users/gunju/Desktop/self study/python/chromedriver", chrome_options = chrome_options)
browser.maximize_window()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

browser.switch_to.frame("iframeResult")

elem = browser.find_element(By.XPATH, '//*[@id="html"]')

# 선택이 안 되어 있으면 선택하기
if elem.is_selected() == False:
    print("선택 안 되어 있으므로 선택하기")
    elem.click()
else:
    print("선택되어 있으므로 아무것도 안 함")

time.sleep(5)

if elem.is_selected() == False:
    print("선택 안 되어 있으므로 선택하기")
    elem.click()
else:
    print("선택되어 있으므로 아무것도 안 함")

browser.quit()