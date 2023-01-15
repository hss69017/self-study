my_set = {1, 2, 3, 3, 3}  #중복 X, 순서 X
print(my_set)

java = {"a", "b", "c"}
python = set(["a", "d"])

print(java & python)
print(java.intersection(python))

print(java | python)
print(java.union(python))

print(java - python)
print(java.difference(python))

python.add("b")
print(python)

java.remove("b")
print(java)