t = int(input("Enter the number of test cases:"))
for i in range(0, t):
    try:
        a = int(input())
        b = int(input())
        print(a // b)
    except ZeroDivisionError:
        print("Error Code: Integer division or modulo by zero")
    except ValueError:
        print("Error Code: Invalid literal for int() with base 10:", b)
