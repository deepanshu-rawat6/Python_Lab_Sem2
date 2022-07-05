str1 = input()
s = str1.split()
new_str = ""
for i in range(0, len(s) - 1):
    str1 = s[i]
    new_str = new_str + (str1[0].upper() + '.')
new_str = new_str + ' ' + s[len(s) - 1].capitalize()
print(new_str)
