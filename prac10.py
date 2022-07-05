str=input()
str=str.lower()
x=str.count('a')
print(x)
print()
c=0
for i in range(0,len(str)):
    if str[i]=='a':
        c=c+1
print(c)
