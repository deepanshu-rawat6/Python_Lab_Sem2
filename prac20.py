def product(x):
    prod = 1
    for i in x:
        prod *= i
    return prod


lst = [1, 2, 3, 4, 5]
print(product(lst))


