from abc import ABC, abstractmethod

class Transaction(ABC):
    def __init__(self, amount, description=""):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.amount = amount
        self.description = description

    @abstractmethod
    def apply(self, wallet):
        pass

class Income(Transaction):
    def apply(self, wallet):
        wallet._update_balance(self.amount)

class Expense(Transaction):
    def apply(self, wallet):
        if wallet.get_balance() >= self.amount:
            wallet._update_balance(-self.amount)
        else:
            raise ValueError("Insufficient balance for expense")