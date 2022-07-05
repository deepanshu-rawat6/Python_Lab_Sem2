dict1 = {}
list1 = []
n = int(input())
i = 0
name = ""
for i in range(n):
    name = input()
    for j in range(n):
        num = int(input())
        list1.append(num)
    dict1[name] = list1
    list1 = []
list2 = dict1[name]
print("%.2f" % (sum(list2) / n))
