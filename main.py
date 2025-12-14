from wallet.wallet import Wallet
from wallet.transaction import Income, Expense

def main():
    wallet = Wallet()

    wallet.add_transaction(Income(10000, "Salary"))
    wallet.add_transaction(Expense(2500, "Groceries"))
    wallet.add_transaction(Expense(1200, "Internet Bill"))

    print(wallet)

if __name__ == "__main__":
    main()