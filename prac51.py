f = open("temp.txt", "r")
obj = f.readlines()
list1 = []
list2 = []
str1 = ""
add = 0
c = 0
mini = 0
for line in obj:
    c = c + 1
    a = 0
    list1 = line.split()
    print('Product:{}\t{}\t{}\t{}\t{}'.format(list1[0], list1[1], list1[2], list1[3], list1[4]))
    for i in range(1, 5):
        a = a + float(list1[i])
    add = add + a
    if mini == 0:
        mini = a
    if mini > a:
        mini = a
        str1 = list1[0]
print()
print("The average sales of the all products:", (add / c))
print("The product with minimum sales:", str1)
