mylist = [1, 2, 3, '4', 5]

try:
    sum = 0
    for i in mylist:
        sum = sum + i
    print(sum)
except TypeError:
    print("Cannot operate on variables of different type!")
try:
    print(mylist[5])
except IndexError:
    print("Index out of range!")
