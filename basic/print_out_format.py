print("{0: >10}".format(500)) #빈 자리(space 한 곳)는 빈 공간으로 두고, 오른쪽 정렬(>)을 하되, 총 10자리 공간을 확보

#if it is positive number, then write +, if not, then write - 
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬, 빈칸 _ 으로 채움
print("{0:_<+10}".format(500))

# 3자리마다 , 찍기
print("{0:,}".format(1000000000000))

# 3자리마다 ,찍고, +-부호
print("{0:+,}".format(1000000000000))
print("{0:+,}".format(-1000000000000))

#3자리마 콤마 찍고, 부호 붙이고, 자리수 확보, 빈자리는 ^
print("{0:^<+30,}".format(100000000000000))

#소수점
print("{0:f}".format(5/3))

#소수점을 특정 자리수까지만 표시
print("{0:.2f}".format(5/3)) # 반올림