class Student:
    def __init__(self):
        self.m2 = None
        self.m3 = None
        self.m1 = None
        self.rollno = None
        self.c_lass = None
        self.stuname = None

    def details(self):
        self.stuname = input()
        self.c_lass = input()
        self.rollno = input()
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
        print("Student name:", self.stuname)
        print("Class:", self.c_lass)
        print("Roll_no:", self.rollno)
        print("Marks 1:", self.m1)
        print("Marks 2:", self.m2)
        print("Marks 3:", self.m3)
        print("Faculty name:", self.faculty_name)
        print("%age:", (self.m1 + self.m2 + self.m3) / 3)


Obj = result()
Obj.details()
Obj.name()
Obj.compute()
