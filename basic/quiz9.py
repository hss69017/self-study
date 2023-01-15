class SoldOutError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    try:
        print("[the remaining chicken(s): {0}]".format(chicken))
        order = int(input("How many chickens do you order? "))
        if order > chicken:
            print("There is(are) not enough chicken(s).")
        elif order < 1:
            raise ValueError
        else:
            print("[waiting number {0}] You ordered {1} chicken(s).".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("You typed something wrong.")
    except SoldOutError:
        print("There is no chicken. I can't receive an order.")
        break