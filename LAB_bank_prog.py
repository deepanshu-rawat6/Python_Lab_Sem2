def deposit(acc):
    f = open(acc + ".txt", "r")
    amt = input("Enter the amount to be deposited:")
    content = f.read()
    print("Current Balance:%s" % float(content))
    f.close()
    f = open(acc + ".txt", "w+")
    c = str(float(content) + float(amt))
    f.write(c)
    f.close()
    f = open(acc + ".txt", "r")
    print("Updated Balance:%s" % (f.read()))
    f.close()


def withdraw(acc):
    f = open(acc + ".txt", "r")
    amt = input("Enter the amount to be withdrawn:")
    content = f.read()
    print("Current Balance:%s" % float(content))
    f.close()
    if float(content) >= float(amt):
        c = str(float(content) - float(amt))
        f = open(acc + ".txt", "w+")
        f.write(c)
        f.close()
        f = open(acc + ".txt", "r")
        print("Updated Balance:%s" % (f.read()))
        f.close()
    else:
        print("Insufficient Balance!")


acc = input("Enter the account number:")
n = int(input("Enter 1 for deposit or 2 for withdraw:"))
if n == 1:
    deposit(acc)
else:
    withdraw(acc)
