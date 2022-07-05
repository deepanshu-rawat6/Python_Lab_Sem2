class Account:
    def fun(self, initial_balance):
        self.__balance = initial_balance

    def withdraw(self, amount):
        self.__balance -= amount

    def deposit(self, amount):
        self.__balance += amount

    def display(self):
        print(self.__balance)


ac = Account()
ac.fun(1000)
ac.withdraw(100)
ac.display()
ac.balance = -1000
print(ac.balance)
