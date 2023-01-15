import pyautogui
import pyperclip

# 메모 프로그램 실행
icon_memo = pyautogui.locateOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/12_quiz/icon_memo.png", confidence = 0.8)
a = icon_memo
pyautogui.click((a[0] / 2, a[1] / 2, a[2] / 2, a[3] / 2))

# 프로그램 창 최대화 / mac에서는 구현되지 않는 기능이기 때문에 주석으로만 작성
# pyautogui.sleep(1) # 프로그램 실행 시간 고려 1초 대기
# program_menu = pyautogui.getActiveWindow()
# program_menu.maximize()

# 새 파일 만들기
icon_new_file = pyautogui.locateOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/12_quiz/icon_new_file.png", confidence = 0.7)
b = icon_new_file
pyautogui.click((b[0] / 2, b[1] / 2, b[2] / 2, b[3] / 2))

# 글자 입력
pyperclip.copy("참 잘했어요")
pyautogui.hotkey("command", "command", "v")

# 5초 대기 후 메모 프로그램 종료
pyautogui.sleep(5)
pyautogui.hotkey("command", "command", "q")