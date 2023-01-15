students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["Ironman", "Thor", "Iamgroot"]
students = [len(i) for i in students]
print(students)

students = ["Ironman", "Thor", "Iamgroot"]
students = [i.upper() for i in students]
print(students)