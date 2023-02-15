class bank:
    def __init__(self):
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount

    def withdraw(self,amount):
        self.amount = amount
        if self.amount <= self.balance:
            print("Withdrawal sucessful")
            self.balance =  self.balance - self.amount
        else:
            print("Insufficient Balance")
    def display(self):
        print("Your balance is: ",self.balance)

s1 = bank()
