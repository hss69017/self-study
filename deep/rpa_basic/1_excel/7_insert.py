from openpyxl import load_workbook
wb = load_workbook("/Users/gunju/Desktop/self study/python/deep/rpa_basic/1_excel/sample.xlsx")
ws = wb.active

# ws.insert_rows(8) # 8번째 줄에 추가
# ws.insert_rows(8, 5) # 8번째 줄 위치에 5줄 추가
# wb.save("/Users/gunju/Desktop/self study/python/deep/rpa_basic/1_excel/sample_insert_rows.xlsx")

# ws.insert_cols(2)
ws.insert_cols(2, 3)
wb.save("/Users/gunju/Desktop/self study/python/deep/rpa_basic/1_excel/sample_insert_cols.xlsx")