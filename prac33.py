# Strings are immutable.
string1 = "Hello World!"
print(string1)
for i in string1:
    print(i, end=' ')
print("\n")
print(len(string1))
print("Hello" in string1)
print(string1[-2])  # just like lists we can use negative indexing in strings
