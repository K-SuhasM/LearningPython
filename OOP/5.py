class Bankaccounts:
    MIN_BALANCE = 100

    def __init__(self, name, balance, age):
        self.name = name 
        self.balance = balance
        self.age = age

    def deposit(self, amount):
        if amount>0:
            self.balance += amount
        else:
            print("Amount must be non zero and positive")
        print(f" New blance of {self.name} is {self.balance}")

    @staticmethod
    def is_valid_age(value):
        if value >= 18:
            print("Age is valid")
        else: print("Age is not valid")


c1 = Bankaccounts("Raj", 500, 50)
c2 = Bankaccounts("sam", 00, 17)

c1.deposit(500)
Bankaccounts.is_valid_age(19)