#지역변수(local variable), 전역변수(global variable)
#함수 내에 있는 것이 지역변수, 함수밖에 있는 것을 사용할 때 global을 붙여서 사용하면 전역변수

gun = 10

def checkpoint(soldiers): #경계근무(guard)
    global gun # using global variable "gun" in global area
    # if I use local variable "gun" which means without "global", "gun" in definion differs from "gun" outside definition
    gun = gun - soldiers
    print("[in definition] the remaining gun(s): {0}".format(gun))

# print("total gun(s): {0}".format(gun))
# checkpoint(2)
# print("the remaining gun(s): {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[in definition] the remaining gun(s): {0}".format(gun))
    return gun

print("total gun(s): {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("the remaining gun(s): {0}".format(gun))