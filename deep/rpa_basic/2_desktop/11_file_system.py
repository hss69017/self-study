# 파일 기본
import os

# print(os.getcwd()) # current working directory
# os.chdir("deep") # 현재 폴더 밑에 있는 ~로 이동
# print(os.getcwd())
# os.chdir("..") # 상위폴더로 이동
# print(os.getcwd())
# os.chdir("../..") # 상위폴더의 상위폴더로 이동
# print(os.getcwd())
# os.chdir("/Users") # 절대경로도 가능
# print(os.getcwd())

# 파일 경로
# file_path = os.path.join(os.getcwd(), "deep/rpa_basic/2_desktop/my_file.txt") # 절대경로 생성
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/my_file.txt"))

# 파일 정보 가져오기
# import time
# import datetime

# # 파일의 생성 날짜(실제 생성날짜라기보다는 inode 변경이 발생했을 때)
# ctime = os.path.getctime("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/run_btn.png")
# print(ctime) # 이러면 알아볼 수 없는 포맷으로 나옴
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/run_btn.png")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/run_btn.png")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# # 파일 크기
# size = os.path.getsize("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/run_btn.png") # byte
# print(size)

# 파일 목록 가져오기
# print(os.listdir()) # 현재 경로의 모든 폴더, 파일 목록 가져오기
# print(os.listdir("deep/rpa_basic"))

# 하위폴더 포함 파일 목록 가져오기
# result = os.walk("deep/rpa_basic") # <generator object _walk at 0x1030a1740> 이런 식으로 나옴 / 현재 폴더로 가져오고 싶으면 "."
# # print(result)

# for root, dirs, files in result:
#     print(root, dirs, files) # 폴더, [하위폴더들], [파일들]

# 만약 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk(os.getcwd()):
#     if name in files:
#         result.append(os.path.join(root, name))
# print(result)

# 만약 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# *.xlsx, *.txt, 자동화*.png
# import fnmatch

# pattern = "*.py"
# result = []
# for root, dirs, files in os.walk("."):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern): # name과 pattern이 일치한다면
#             result.append(os.path.join(root, name))
# print(result)

# 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir("/Users/gunju/Desktop/self study/python/deep/rpa_basic"))
# print(os.path.isfile("/Users/gunju/Desktop/self study/python/deep/rpa_basic"))

# print(os.path.isdir("/Users/gunju/Desktop/self study/python/chromedriver"))
# print(os.path.isfile("/Users/gunju/Desktop/self study/python/chromedriver"))

# # 만약에 지정된 경로에 해당하는 파일 / 폴더가 없다면?
# print(os.path.isfile("run_btnnnn.png")) # 없는 파일이면 False 반환

# 주어진 경로가 존재하는지?
# if os.path.exists("/Users/gunju/Desktop/self study/python/deep/rpa_basic"):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")

# 파일 만들기
# open("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/new_file.txt", "a").close()

# 파일명 변경하기
# os.rename("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/new_file.txt", "/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/new_file_rename.txt")

# 파일 삭제
# os.remove("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/new_file_rename.txt")

# 폴더 만들기
# os.mkdir("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/new_folder")

# os.mkdir("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/new_folders/a/b/c") # 하위폴더를 가지는 폴더 생성 시도: 실패
# os.makedirs("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/new_folders/a/b/c") # 성공

# 폴더명 변경하기
# os.rename("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/new_folder", "/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/new_folder_rename")

# 폴더 지우기
# os.rmdir("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/new_folder_rename") # 폴더 안이 비어있을 때만 삭제 가능

import shutil

# shutil.rmtree("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/new_folders") # 폴더 안이 비어있지 않아도 삭제 가능, 주의!

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/run_btn.png", "/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder")
# 파일 복사 후 복사된 파일명 변경
# shutil.copy("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/run_btn.png", "/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder/copied_run_btn.png")

# shutil.copy와의 차이점은 copyfile은 2번째 인자에 파일만 쓸 수 있다. 폴더는 쓸 수 없다.
# shutil.copyfile("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/run_btn.png", "/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder/copied_run_btn_2.png")

# copy, copyfile: 메타정보 복사 x
# copy2: 메타정보 복사 o
# shutil.copy("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/run_btn.png", "/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder/copy.png")
# shutil.copy2("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/run_btn.png", "/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder/copy2.png")

# 폴더 복사
# shutil.copytree("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder", "/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder2")
# shutil.copytree("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder", "/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder3")

# 폴더 이동 / 첫번째 인자 폴더를 두 번째 인자 폴더 경로 밑으로 이동
# shutil.move("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder", "/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder3")
# shutil.move("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder2", "/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder3")
# 2번째 인자를 없는 폴더로 지정할 경우 폴더명을 변경하는 효과
shutil.move("/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder3", "/Users/gunju/Desktop/self study/python/deep/rpa_basic/2_desktop/test_folder")
