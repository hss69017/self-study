menu = {"coffee", "milk", "juice"}
print(menu, type(menu)) # {'juice', 'coffee', 'milk'} <class 'set'>

menu = list(menu)
print(menu, type(menu)) # ['juice', 'coffee', 'milk'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('juice', 'coffee', 'milk') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) # {'juice', 'coffee', 'milk'} <class 'set'>