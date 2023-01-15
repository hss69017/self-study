from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image("/Users/gunju/Desktop/self study/python/deep/rpa_basic/1_excel/img.png")

# C3 위치에 img.png 파일 이미지 삽입
ws.add_image(img, "C3")
wb.save("/Users/gunju/Desktop/self study/python/deep/rpa_basic/1_excel/sample_image.xlsx")

# 이것을 하려면 pillow package를 설치해야 함