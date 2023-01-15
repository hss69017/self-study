from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome("/Users/gunju/Desktop/self study/python/chromedriver", options = chrome_options)
browser.maximize_window()

# w3school 접속
browser.get("https://www.w3schools.com/")

# LEARN HTML 클릭
browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

# HOW TO 클릭
browser.find_element(By.XPATH, '//*[@id="topnav"]/div/div[1]/a[11]').click()

# Contact Form 클릭
time.sleep(2)
browser.find_element(By.XPATH, '//*[@id="leftmenuinnerinner"]/a[118]').click()

# 입력
first_name = "GJ"
last_name = "Im"
country = "Canada"
subject = "퀴즈 완료하였습니다."

browser.find_element(By.XPATH, '//*[@id="fname"]').send_keys(first_name)
browser.find_element(By.XPATH, '//*[@id="lname"]').send_keys(last_name)
browser.find_element(By.XPATH, '//*[@id="country"]/option[text()="{}"]'.format(country)).click()
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/textarea').send_keys(subject)

# 5초 대기 후 submit 클릭
time.sleep(5)
browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a').click()

# 5초 대기 후 브라우저 종료
time.sleep(5)
browser.quit()