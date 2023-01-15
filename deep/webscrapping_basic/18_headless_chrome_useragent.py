from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=2560x1600")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")

browser = webdriver.Chrome("/Users/gunju/Desktop/self study/python/chromedriver", options = options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)

# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
detected_value = browser.find_element(By.ID, "detected_value")
print(detected_value.text)
# headless일 때는 Chrome/108.0.0.0 이 부분이 HeadlessChrome~ 이런 식으로 바뀜
# 따라서 7번째 줄 user-agent 정보를 적어주면 user-agent 정보가 적용되어 headless로 안뜸
browser.quit()