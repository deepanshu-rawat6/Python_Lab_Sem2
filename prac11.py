str=input()
vowel = set("aeiouAEIOU")
c=0
for i in str:
    if i in vowel:
        c=c+1
print(c)
