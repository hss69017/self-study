print("Python", "Java", sep = ",", end = "?") # sep는 구분 구문, end는 문장 줄 안바꾸고 안에 있는 구문 이용
print("Which is funnier?")

import sys
print("Python", "Java", file = sys.stdout)
print("Python", "Java", file = sys.stderr)

scores = {"math": 0, "english": 50, "coding": 100} #dictionary
for subject, score in scores.items():
    print(subject.ljust(7), str(score).rjust(3), sep = ": ") #ljust, rjust는 출력을 이쁘게 만듬 좌우측 공간 확보하여 정렬

for num in range(1, 21):
    print("waiting number: " + str(num).zfill(3)) #zfill은 해당만큼 공간을 확보하고, 빈공간은 0으로 채움

answer = input("Type anything: ") #input은 문자형으로 받음
print(type(answer))
print("What you typed is " + answer + ".") #answer에 문자형이 아닌 숫자형이 들어가도 정상 출력됨