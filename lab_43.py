str1 = input()
str1 = str1.upper()
individual = set(str1)
individual = sorted(individual)
for i in individual:
    c = str1.count(i)
    print("%d %c" % (c, i))
