class Student:
    def __init__(self):
        self.stu_name = None
        self.m2 = None
        self.m3 = None
        self.m1 = None
        self.roll_no = None
        self.clllass = None

    def details(self):
        self.stu_name = input()
        self.clllass = input()
        self.roll_no = int(input())
        self.m1 = int(input("Enter the marks of sub 1:"))
        self.m2 = int(input("Enter the marks of sub 2:"))
        self.m3 = int(input("Enter the marks of sub 3:"))


class Faculty:
    def __init__(self):
        self.faculty_name = None

    def name(self):
        self.faculty_name = input("Enter the faculty name:")


class result(Student, Faculty):
    def compute(self):
        print("\n")
        print("Student name:", self.stu_name)
        print("Class:", self.clllass)
        print("Roll_no:", self.roll_no)
        print("Marks 1:", self.m1)
        print("Marks 2:", self.m2)
        print("Marks 3:", self.m3)
        print("Faculty name:", self.faculty_name)
        print("%age:", (self.m1 + self.m2 + self.m3) / 3)


Obj = result()
Obj.details()
Obj.name()
Obj.compute()
