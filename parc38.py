import math

class Base:
    def __init__(self):
        self.l = int(input("Enter the length:"))
        self.b = int(input("Enter the breadth:"))
        self.r = int(input("Enter the radius:"))

    def rectangle(self):
        return self.l * self.b

    def circle(self):
        return math.pi * self.r ** 2


obj = Base()
n = int(input("Enter 1 for rectangle and 2 for circle:"))
print("\n")
if n == 1:
    print("Area of rectangle:", obj.rectangle())
else:
    print("Area of circle:", obj.circle())
