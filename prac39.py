class SI:
    def __init__(self, r):
        self.r = r
        self.p = int(input("Enter the principal:"))
        self.t = int(input("Enter the time:"))

    def compute(self):
        print("Simple Interest:", ((self.p * self.r * self.t) / 100))


r = 6
obj = SI(6)
obj.compute()
