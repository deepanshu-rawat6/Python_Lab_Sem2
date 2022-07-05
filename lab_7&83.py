f = open("city.txt", "r+")
y = f.readlines()
list2 = []
sum = 0
for i in y:
    list1 = i.split()
    print('NAME:{}\tPOPULATION:{}\tAREA:{}'.format(list1[0], list1[1], list1[2]))
    sum = sum + float(list1[2])
    if float(list1[1]) > 10:
        list2.append(list1[0])

print("City names with population more than 10 Lakhs:")
print(list2)
print("sum of areas of all cities:")
print(sum)
