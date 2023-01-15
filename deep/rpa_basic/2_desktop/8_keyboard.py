import pyautogui

# write: 한글은 못 적는다. 영문 / 숫자만 쓸 수 있음
# pyautogui.write("12345") # 글자 쓰기
# pyautogui.write("GJCoding", interval = 1) # interval: 1초에 한 글자씩 쓰기

# left: 화살표 왼쪽, right: 화살표 오른쪽, enter: 엔터키
# https://automatetheboringstuff.com/2e/chapter20/
# keyboard attribute 검색
# pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "enter"])

# 특수문자 (shift + ~)
# pyautogui.keyDown("shift")
# pyautogui.press("4")
# pyautogui.keyUp("shift")

# 조합키 (Hot Key)
# pyautogui.keyDown("command")
# pyautogui.keyDown("a")
# pyautogui.keyUp("a")
# pyautogui.keyUp("command")

# 간편한 조합키 / 왜인지 모르겠으나 "command"가 맨 처음에 있으면 그 command는 안 먹히는듯하다
# pyautogui.hotkey("command", "command", "a")

# pip3 install pyperclip
import pyperclip

# pyperclip.copy("GJ") # ~ 글자를 클립보드에 저장
# pyautogui.hotkey("command", "command", "v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("command", "command", "v")

my_write("GJ")

# pyautogui 자동화 프로그램 종료 키보드로 할 때
# win: ctrl + alt + del
# mac: cmd + shift + option + q