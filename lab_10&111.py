class Employee:
    def __init__(self):
        self.first_name = input("Enter the first name:")
        self.last_name = input("Enter the last name:")
        self.pay = input("Enter the pay:")

    def display(self):
        print("First name:", self.first_name)
        print("Last name:", self.last_name)
        print("Pay:", self.pay)
        s = self.first_name + "." + self.last_name + "@outlook.com"
        print("Email Address:", s)


obj = Employee()
print("\n")
obj.display()
