def max_two(x, y):
    if x > y:
        return x
    return y


def max_three(x, y, z):
    return max_two(x, max_two(y, z))


x = int(input("Enter the number:"))
y = int(input("Enter the number:"))
z = int(input("Enter the number:"))
print(max_three(x, y, z))
