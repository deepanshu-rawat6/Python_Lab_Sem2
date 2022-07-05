class Data:
    """Report Card"""

    def accept(self):
        self.a = int(input("Enter the marks:"))
        self.b = int(input("Enter the marks:"))
        self.c = int(input("Enter the marks:"))

    def calculate(self):
        self.accept()
        d=(self.a + self.b + self.c) / 3
        print("Percentage:", d)


S1 = Data()
S1.calculate()

S2 = Data()
S2.calculate()
