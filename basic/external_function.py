#search "list of python modules" on Google

# import glob # 경로 내의 폴더 / 파일 목록 조회
# print(glob.glob("*.py"))

# import os # 운영체제에서 제공하는 기본 기능(폴더 생성, 삭제 등)
# print (os.getcwd()) # 현재 디렉토리

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("The folder exists.")
#     os.rmdir(folder)
#     print(folder, "The folder is deleted.")
# else:
#     os.makedirs(folder) # creating folder
#     print(folder, "A folder is created.")

# print(os.listdir()) # glob와 비슷

# import time # concerning time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("Today is", datetime.date.today())
today = datetime.date.today()
td = datetime.timedelta(days = 100) # 100일 저장, 두 날짜 사이의 간격 계산 시 사용
print("The day we meet for 100 days is", today + td)