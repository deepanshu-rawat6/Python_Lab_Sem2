# A list is a collection of data, which can hold multiple values of different data types.
# The list is mutable and stores data in an ordered form, and allow duplicates.
list1 = [1, 2, 3, 4, 5, 6]
print(list1)
list1[0] = 100  # list are mutable and can be modified by using assignment operator
print(list1)
print(len(list1))
print("The element at 4th index:%d" % (list1[3]))
list1.append(1)
print(list1)  # list can allow duplicates
