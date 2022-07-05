import random
#n=input("Enter the starting point:")
#m=input("Enter the ending point:")
x=random.randint(10,30)
y=random.randint(10,30)
z=random.randint(10,30)
if x==y and x==z:
    print("First Prize")
elif x==y or y==z or x==z:
    print("Second Prize")
else:
    print("Try again")
print("%d %d %d" %(x,y,z))
