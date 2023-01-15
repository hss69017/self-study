# score_file = open("score.txt", "w", encoding = "utf8") #덮어쓰기
# print("수th: 0", file = score_file)
# print("english: 50", file = score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding = "utf8") #더하기
# score_file.write("science: 80")
# score_file.write("\ncoding: 100") #\n은 줄바꿈
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8") #reading everything
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8")
# print(score_file.readline(), end="") # 한 줄씩 읽고, 커서는 다음줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8") #몇 줄일지 모를때 읽을때
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines() #모든 라인 가져와서 list 형태로 저장
for line in lines:
    print(line, end = "")
score_file.close()