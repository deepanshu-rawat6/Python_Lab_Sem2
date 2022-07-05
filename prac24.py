def solve(x):
    ch = x[0]
    str1 = x.replace(ch, "$")
    str1 = ch + str1[1:]
    return str


str2 = input("Enter the string:")
print(solve(str2))

# solve on own
