n = int(input("N ="))
list1 = []
maximum = 0
for i in range(0, n):
    element = int(input("Scores:"))
    list1.append(element)
    if element > maximum:
        maximum = element
list1.sort()
for i in range(n - 1, -1, -1):
    if maximum != list1[i]:
        maximum = list1[i]
        break
print("\n")
print(maximum)
