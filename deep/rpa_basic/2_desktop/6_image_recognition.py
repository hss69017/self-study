import pyautogui

# file_menu = pyautogui.locateOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/file_menu.png")
# # 해당 이미지를 스크린에서 찾으면 위치 좌표와 넓이, 높이를 반환 / 다만 mac에서는 각 값을 2로 나눠줘야 함
# print(file_menu)
# pyautogui.click((file_menu[0] / 2, file_menu[1] / 2, file_menu[2] / 2, file_menu[3] / 2))
# # 이렇게 되면 스크린에서 찾은 이미지 부분에 정가운데를 클릭하게 됨

# trash_icon = pyautogui.locateOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/trash_icon.png")
# pyautogui.moveTo((trash_icon[0] / 2, trash_icon[1] / 2, trash_icon[2] / 2, trash_icon[3] / 2))

# screen = pyautogui.locateOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/screenshot.png")
# print(screen) # 이미지를 찾지 못 하면 None을 반환

# locateAllOnScreen: 스크린 상에 이미지와 같은 모든 것을 가져옴 / locateOnScreen: 처음 찾는 것만 가져옴
# for i in pyautogui.locateAllOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/checkbox.png"):
#     print(i)
#     pyautogui.click((i[0] / 2, i[1] / 2, i[2] / 2, i[3] / 2), duration = 0.25)

# checkbox = pyautogui.locateOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/checkbox.png")
# pyautogui.click((checkbox[0] / 2, checkbox[1] / 2, checkbox[2] / 2, checkbox[3] / 2))

# trash_icon = pyautogui.locateOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/trash_icon.png")
# pyautogui.moveTo((trash_icon[0] / 2, trash_icon[1] / 2, trash_icon[2] / 2, trash_icon[3] / 2))

# 속도 개선
# 1. GrayScale: 흑백으로 전환 후 이미지 찾기, 30% 속도 개선, 정확도는 떨어질 수 있음
# trash_icon = pyautogui.locateOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/trash_icon.png", grayscale = True)
# pyautogui.moveTo((trash_icon[0] / 2, trash_icon[1] / 2, trash_icon[2] / 2, trash_icon[3] / 2))

# 2. 범위 지정 / mac에서는 * 2를 해줘야 함
# trash_icon = pyautogui.locateOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/trash_icon.png", region = (953 * 2, 521 * 2, 322 * 2, 120 * 2))
# pyautogui.moveTo((trash_icon[0] / 2, trash_icon[1] / 2, trash_icon[2] / 2, trash_icon[3] / 2))

# 3. 정확도 조정 / # pip3 install opencv-python / confidence 기본값은 0.999
# run_btn = pyautogui.locateOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/run_btn.png", confidence = 0.9)
# pyautogui.moveTo((run_btn[0] / 2, run_btn[1] / 2, run_btn[2] / 2, run_btn[3] / 2))

# 자동화 대상이 바로 보여지지 않는 경우 / 현재 스크린에는 없으나 곧 뜰 때까지 기다려야 하는 경우를 얘기함
# 1. 계속 기다리기
# word_notepad = pyautogui.locateOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/word_notepad.png")
# if word_notepad:
#     pyautogui.click(word_notepad)
# else:
#     print("발견 실패")
# while word_notepad is None:
#     word_notepad = pyautogui.locateOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/word_notepad.png")
#     print("발견 실패")

# pyautogui.click((word_notepad[0] / 2, word_notepad[1] / 2, word_notepad[2] / 2, word_notepad[3] / 2))

# 2. 일정 시간 동안 기다리기 (TimeOut)
import time
import sys

# timeout = 10 # 10초 대기
# start = time.time() # 시작시간
# word_notepad = None
# while word_notepad is None:
#     word_notepad = pyautogui.locateOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/word_notepad.png")
#     end = time.time() # 종료시간
#     if end - start > timeout:
#         print("시간 종료")
#         sys.exit() # 프로그램 종료

def find_target(img_file, timeout):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/word_notepad.png")
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click((target[0] / 2, target[1] / 2, target[2] / 2, target[3] / 2))
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

# pyautogui.click((word_notepad[0] / 2, word_notepad[1] / 2, word_notepad[2] / 2, word_notepad[3] / 2))

my_click("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/word_notepad.png", 10)