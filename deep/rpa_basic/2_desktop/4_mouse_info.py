import pyautogui
# pyautogui.FAILSAFE = False # 마우스를 모서리에 옮겨도 프로그램이 계속 실행되는 옵션
pyautogui.PAUSE = 1 # 모든 동작에 1초씩 sleep 적용
# pyautogui.mouseInfo() # 마우스 위치 등 정보를 알려주는 프로그램이 실행됨 / mac은 색 정보를 가져오지 못함

for i in range(10):
    pyautogui.move(100, 100)
    # pyautogui.sleep(1)
    # 이 때 마우스를 모니터 4개의 모서리 중 한 군데로 옮기면 FailSafeException이 출력되면서 프로그램이 종료됨