# RPA: Robotic Process Automation 업무자동화

# pip3 install openpyxl
# 학습 사이트: https://openpyxl.readthedocs.io/en/stable/

from openpyxl import Workbook
wb = Workbook() # 새 워크북 생성(엑셀 파일)
ws = wb.active # 현재 활성화된 sheet 가져옴
ws.title = "GJSheet" # sheet 이름 변경
wb.save("/Users/gunju/Desktop/self study/python/deep/rpa_basic/1_excel/sample.xlsx") # "~" 이름으로 파일 저장
wb.close() # 파일 닫기