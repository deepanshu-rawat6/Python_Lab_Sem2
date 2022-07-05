def solve(n, m):
    lst = []
    for i in range(n, m + 1):
        lst.append(i*i)
    return lst


a = int(input("Enter the starting point:"))
b = int(input("Enter the ending point:"))

print(solve(a, b))
