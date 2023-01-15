# 정규식(regular expression)
# w3school - python -regex: learning
# python re: learning, official document

import re

p = re.compile("ca.e")
# . (ca.e): 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de): 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$): 문자열의 끝 > case, base (O) | face (X)

def print_match(m):
    if m:
        print("m.group():", m.group()) # group(): 일치하는 문자열 반환, 매칭되면 결과 반환, 매칭되지 않으면 에러가 발생
        print("m.string:", m.string) # string: 입력받은 문자열, 얘만 함수가 아닌 변수
        print("m.start():", m.start()) # start(): 일치하는 문자열의 시작 index
        print("m.end():", m.end()) # end(): 일치하는 문자열의 끝 index + 1
        print("m.span():", m.span()) # span(): 일치하는 문자열의 시작 / 끝 + 1 index
    else:
        print("They don't match.")

# m = p.match("cafe") # 주어진 문자열의 처음부터 일치하는지 확인 / 뒷부분에 다른 것이 있어도 상관없음. careless도 매치로 나옴
# print_match(m)

# m = p.search("good care") # search: 주어진 문자열 중에 일치하는게 있는지 확인
# print_match(m)

lst = p.findall("good care cafe") # findall: 일치하는 모든 것을 리스트 형태로 반환
print(lst)

# 1. p = re.compile("원하는 정규식 형태")
# 2. m = p.match("비교할 문자열") or m = p.search("~") or lst = p.findall("~")

# 원하는 정규식 형태
# . (ca.e): 하나의 문자를 의미 > care, cafe, case (O) | caffe (X)
# ^ (^de): 문자열의 시작 > desk, destination (O) | fade (X)
# $ (se$): 문자열의 끝 > case, base (O) | face (X)