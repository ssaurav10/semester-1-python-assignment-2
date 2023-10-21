"""

#question

"""


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount. Amount must be greater than 0."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid withdrawal amount or insufficient balance."

    def check_balance(self):
        return f"Account balance for {self.owner}: ${self.balance}"

    def transfer(self, other_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            other_account.balance += amount
            return f"Transferred ${amount} from {self.owner} to {other_account.owner}. New balance for {self.owner}: ${self.balance}"
        else:
            return "Invalid transfer amount or insufficient balance."

account1 = BankAccount("John Doe", 1000)
account2 = BankAccount("Jane Smith", 500)

print(account1.check_balance())
print(account2.check_balance())

print(account1.deposit(200))
print(account2.deposit(300))

print(account1.withdraw(50))
print(account2.withdraw(200))

print(account1.transfer(account2, 150))

print(account1.check_balance())
print(account2.check_balance())
