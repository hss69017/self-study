# <html>
#     <body>
#         # iframe: 프레임으로 페이지를 나눔, 그래서 아래는 <html>부터 새로 써짐
#         # xpath로 아래 있는 것들을 바로 찾을 때는 찾을 수가 없기 때문에 <iframe>을 찾고, 거기서부터 다시 xpath를 찾아 나가는 식으로 접근해야 한다.
#         <iframe id = "1"> 
#             <html>
#                 <body>
#                     <div...>
#                 </body>
#             </html>
#         </iframe>

#         <iframe id = "2">
#             <html>
#                 <body>
#                     <div...>
#                 </body>
#             </html>
#         </iframe>
#     </body>
# </html>

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

browser = webdriver.Chrome("/Users/gunju/Desktop/self study/python/chromedriver", chrome_options = chrome_options)

browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")

browser.switch_to.frame("iframeResult") # ~ id를 가진 iframe으로 전환

# //*[@id="html"] / iframe 안에 있는 element
# iframe: 프레임으로 페이지를 나눔, 그래서 아래는 <html>부터 새로 써짐
#         # xpath로 아래 있는 것들을 바로 찾을 때는 찾을 수가 없기 때문에 <iframe>을 찾고, 거기서부터 다시 xpath를 찾아 나가는 식으로 접근해야 한다.
elem = browser.find_element(By.XPATH, '//*[@id="html"]') # 성공

elem.click()

browser.switch_to.default_content() # iframe에 있는 상태에서 상위로 빠져 나옴

elem = browser.find_element(By.XPATH, '//*[@id="html"]') # 실패

elem.click()

time.sleep(5)

browser.quit()