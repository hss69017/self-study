from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("prefs", {"download.default_directory":"/Users/gunju/Desktop/self study/python/deep/rpa_basic/3_web"})

browser = webdriver.Chrome("/Users/gunju/Desktop/self study/python/chromedriver", options = chrome_options)
browser.maximize_window()

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")

browser.switch_to.frame("iframeResult")

# 다운로드 링크 클릭
elem = browser.find_element(By.XPATH, '/html/body/p[2]/a')
elem.click()

time.sleep(2)
browser.quit()