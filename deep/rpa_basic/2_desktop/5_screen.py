import pyautogui

# 스크린샷
# img = pyautogui.screenshot()
# img.save("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 73,7 NA_on_macOS NA_on_macOS

pixel = pyautogui.pixel(73, 7) # 해당 위치의 RGB 값
print(pixel)

# print(pyautogui.pixelMatchesColor(73, 7, (102, 123, 158))) # True, False
print(pyautogui.pixelMatchesColor(73, 7, pixel))