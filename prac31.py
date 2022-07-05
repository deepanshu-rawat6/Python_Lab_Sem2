# A set is mutable, unordered and does not allow duplicates
set1 = {4, 5, 6, 100}
print(set1)

set2 = set("Hello World")
print(set2)

set3 = {1, 2, 3, 4, 1, 2, 3, 4}  # does not allow duplicates
print(set3)

set3.add(6)  # used to add single element in the set
set2.update(['e', 'y', 'u'])  # used to add multiple elements in the set

print(set3)
print(set2)
