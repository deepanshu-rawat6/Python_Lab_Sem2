str1 = input()
sub_str = input()
c = 0
a = len(sub_str)
for i in range(0, len(str1)):
    if str1[i:a] == sub_str:
        c = c + 1
    a = a + 1
    if a > len(str1):
        break
print(c)
