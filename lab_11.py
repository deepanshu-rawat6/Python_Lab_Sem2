# EXPERIMENT -1: Programming Sequential Logic


# Objective: To code sequential logic in Python language


# Q1. Given an integer n, perform the following conditional actions:

# ·        If n is odd, print Weird

# ·        If n is even and in the inclusive range of 2  to 5 , print Not Weird

# ·        If  n is even and in the inclusive range of  6 to 20, print Weird

# ·        If n is even and greater than 20, print Not Weird and if a<10 and a>20

n = int(input("Enter the number:"))
if n % 2 != 0:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    if 6 <= n <= 20:
        print("Weird")
    if n > 20:
        print("Not Weird")
