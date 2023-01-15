# mac에서는 구현이 안 됨

import pyautogui

fw = pyautogui.getActiveWindow() # 현재 활성화된 창
print(fw.title) # 활성화된 창의 제목 정보
print(fw.size) # 창의 크기 정보 (width, height)
print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보
pyautogui.click(fw.left + 10, fw.top + 20)

for w in pyautogui.getAllWindows(): # 모든 창 가져오기
    print(w)

w = pyautogui.getWindowsWithTitle("제목 없음") # ~을 포함하는 제목 정보를 가진 모든 창을 가져옴
print(w)
if w.isAcitve == False: # 현재 활성화가 되지 않았다면
    w.activate() # 활성화

if w.isMaximized == False: # 현재 최대화가 되지 않았다면
    w.maximize() # 최대화
if w.isMinimized == False:
    w.minimize()

w.restore() # 창 원복

w.close() # 창 닫기