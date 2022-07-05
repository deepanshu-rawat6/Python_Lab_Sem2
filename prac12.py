str=input()
str=str.split()
max=0
s=0
for i in str:
    if max<len(i):
        max=len(i)
        s=i
print(s)
print(max)
