def fibo(x):
    b = 1
    c = 0
    for i in range(1, x + 1):
        print(c, end=" ")
        i += 1
        a = b
        b = c
        c = a + b


n = int(input("Enter the number:"))
print("The fibonacci sequence upto %d terms" % n)
fibo(n)
