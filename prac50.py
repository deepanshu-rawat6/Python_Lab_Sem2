class Student:
    def __init__(self):
        self.DoB = None
        self.Mob = None
        self.SAPiD = None
        self.name = None

    def inputt(self):
        self.name = input("Enter the name of the Student:")
        self.SAPiD = input("Enter the SAPiD of the Student:")
        self.DoB = input("Enter the Date of Birth of the Student:")
        self.Mob = input("Enter the Mobile number of the Student:")


class Register(Student):
    def __init__(self):
        super().__init__()
        self.course = None

    def info(self):
        self.course = input("Enter the course name:")

    def display(self):
        print("Student name:", self.name)
        print("SAPiD:", self.SAPiD)
        print("Date of Birth:", self.DoB)
        print("Mobile Number:", self.Mob)
        print("Course Name:", self.course)


obj = Register()
obj.inputt()
obj.info()
print("\n")
obj.display()
