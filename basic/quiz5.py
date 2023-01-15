from random import *

person = 1
customer = 0

while person <= 50:
    time = randrange(5, 51)
    if time <= 15:
        ride = "O"
    else:
        ride = " "
    if ride == "O":
        customer += 1
    print("[{0}] customer {1} (time: {2}min)".format(ride, person, time))
    time = randrange(5, 51)
    person += 1

print("total customer: {0}".format(customer))

# for
customer = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[O] customer {0} (time: {1}min)".format(i, time))
        customer += 1
    else:
        print("[ ] customer {0} (time: {1}min".format(i, time))
print("total customer: {0}".format(customer))