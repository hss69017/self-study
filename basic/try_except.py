try:
    print("calcultor that only can do division")
    nums = []
    nums.append(int(input("Type the first number: ")))
    nums.append(int(input("Type the second number: ")))
    #nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("Error! You typed the wrong thing(s).")
except ZeroDivisionError as err: # "as err" prints the description of error directly.
    print(err)
# except: # 그 밖에 모든 error
#     print("There is an error that can't be known.")
except Exception as err: # 그 밖에 모든 error를 err 문구 그대로 출력
    print("There is an error that can't be known.")
    print(err)