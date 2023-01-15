from random import *

lst = range(1, 21)
lst = list(lst)
shuffle(lst)

winners = sample(lst, 4)

print(" -- winners -- ")
print("chicken: {0}".format(winners[0]))
print("coffee: {0}".format(winners[1:]))
print(" -- Congratulations -- ")