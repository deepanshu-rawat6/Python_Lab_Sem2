import re

str1 = input("Enter the string:")
x = re.findall("\D", str1)
if x:
    print("The string doesn't contain digits")
else:
    print("The string contains digits")
