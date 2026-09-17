class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive"
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance
