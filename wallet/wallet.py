class Wallet:
    def __init__(self):
        self.__balance = 0
        self.transactions = []

    def _update_balance(self, amount):
        self.__balance += amount

    def add_transaction(self, transaction):
        transaction.apply(self)
        self.transactions.append(transaction)

    def get_balance(self):
        return self.__balance
    
    def __str__(self):
        return f"Wallet Balance: {self.__balance}"