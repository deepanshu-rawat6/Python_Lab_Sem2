def add(n):
    if n == 0:
        return 0
    else:
        return n + add(n - 1)


# def fibo(n):
#     if n == 1:
#         return 1
#     elif n == 0:
#         return 0
#     else:
#         return fibo(n - 1) + fibo(n - 2)

def fibo(n):
    a = 0
    b = 1
    sum = 0
    count = 1
    while (count <= n):
        print(sum, end=" ")
        count += 1
        a = b
        b = sum
        sum = a + b


print(add(10))
print()
print(fibo(5))
