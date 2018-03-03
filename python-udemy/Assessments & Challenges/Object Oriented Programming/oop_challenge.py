# For this challenge, create a bank account class that has two attributes:
    # owner
    # balance

# and two methods:
    # deposit
    # withdraw

# As an added requirement, withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: ${self.balance}'

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print('Deposite Accepted')

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print('Withdrawal Accepted')
        else:
            print('Fund Unavailable!')


acct1 = Account('Jose', 100)
print(acct1)

acct1.deposit(50)
print(acct1)

acct1.withdraw(50)
print(acct1)

acct1.withdraw(150)
