class Account(object):
    def __init__(self, name, password, balance=0):
        self.name = name
        self.__password = password
        self.balance = balance

    def deposit(self, money):
        self.balance += money
        return f"Deposited {money}, Balance: {self.balance}"

    def withdraw(self, money):
        if money > self.balance:
            return "Not enough money"
        else:
            self.balance -= money
            return f"Withdrawn {money}, Balance: {self.balance}"

    def transfer(self, acc, money):
        if money > self.balance:
            return "Insufficient funds."
        else:
            self.balance -= money
            acc.balance += money
            return f"Transferred {money} to {acc.name}. Your new balance is {self.balance}."

    def __repr__(self):
        return f"username='{self.name}', balance={self.balance}"


acc1 = Account("George", "gio12356789", 10000)
acc2 = Account("Nika", "pas123451", 50000)

print(acc1.deposit(500))
print(acc1.withdraw(200))
print(acc1.transfer(acc2, 300))
