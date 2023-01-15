from openpyxl import load_workbook
wb = load_workbook("/Users/gunju/Desktop/self study/python/deep/rpa_basic/1_excel/sample.xlsx")
ws = wb.active

# ws.delete_rows(8) # 8번째 줄에 있는 7번 학생 데이터 삭제
# ws.delete_rows(8, 3)
# wb.save("/Users/gunju/Desktop/self study/python/deep/rpa_basic/1_excel/sample_delete_row.xlsx")

# ws.delete_cols(2)
ws.delete_cols(2, 2)

wb.save("/Users/gunju/Desktop/self study/python/deep/rpa_basic/1_excel/sample_delete_col.xlsx")