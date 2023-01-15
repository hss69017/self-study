class BigNumberError(Exception): # my own error
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self): # 에러문구 정의하는 함수
        return self.msg

try:
    print("It's a calculator that can only do division of '1 ~ 9'.")
    num1 = int(input("Type the first number: "))
    num2 = int(input("Type the second number: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("input: {0}, {1}".format(num1, num2)) # making error / ""값은 에러문구 정의
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
    print("You typed the something wrong. Please type the number in '1 ~ 9'.")
except BigNumberError as err:
    print("There is an error. Please type the number in '1 ~ 9'.")
    print(err)
finally: # It prints ~ if there is an error or not.
    print("Thank you for using the calcultor.")