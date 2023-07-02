class Account:
    # attributes
    numCreated = 0
    name = ""
    balance = 0

    # Methods
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.numCreated += 1

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def getbalance(self):
        return self.balance


# new object instances out of template of blueprint

AccountJ = Account("John", 800)
print(AccountJ.name)
print("John: ",AccountJ.balance)

AccountP = Account("Paul", 300)
print(AccountP.name)
print("Paul: ",AccountP.balance)

# reuse methods

AccountP.deposit(50)
print("Paul: ",AccountP.balance)

AccountP.withdraw(100)
print("Paul: ",AccountP.balance)

AccountP.getbalance()
print("Paul: ",AccountP.balance)

AccountJ.deposit(50)
print("John: ",AccountJ.balance)

AccountJ.withdraw(100)
print("John: ",AccountJ.balance)

AccountJ.getbalance()
print("John: ",AccountJ.balance)

