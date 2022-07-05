# WAP to read an integer ‘n’ from STDIN. For all non-negative integers i<n, print i2 on a separate line.

n = int(input("Enter the number:"))
for i in range(0, n):
    print(i * i)
