import pyautogui
# pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position())

# pyautogui.click(125, 15, duration = 1) # 1초 동안 해당 좌표로 이동 후 마우스로 클릭
# pyautogui.click()
# pyautogui.mouseDown() # 마우스로 클릭하고 있는 상태
# pyautogui.mouseUp() # 마우스를 떼고 있는 상태 / click()은 mouseUp()와 mouseDown()을 합친 것 / drag & drop 할 때 쓴다

# pyautogui.doubleClick() # 더블 클릭
# pyautogui.click(clicks = 500) # 클릭을 ~번 연속 하기

# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown()
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp()

pyautogui.sleep(3)
# pyautogui.rightClick() # 마우스 우측 클릭
# pyautogui.middleClick() # 마우스 휠 클릭

# print(pyautogui.position())
# pyautogui.moveTo(951, 302)
# # pyautogui.drag(300, -300, duration = 0.25, button = "left") # 상대 좌표로 이동
# pyautogui.dragTo(1151, 402, button = "left") # 절대 좌표로 이동

pyautogui.scroll(300) # 위 방향으로 300만큼 스크롤 / 음수 값이면 아래 방향