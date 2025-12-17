from users.regular_user import RegularUser
from users.premium_user import PremiumUser
from wallet.transaction import Income, Expense
from payments.upi import UPI
from payments.card import Card
from payments.cash import Cash
from reports.console_report import ConsoleReport

def create_users():
    users = []
    num = int(input("How many users do you want to add? "))

    for i in range(num):
        print(f"\nEnter details for user {i+1}:")
        name = input("Enter name: ")
        email = input("Enter email: ")
        user_type = input("Enter type (regular/premium): ").strip().lower()

        if user_type == "regular":
            user = RegularUser(name, email)
        elif user_type == "premium":
            user = PremiumUser(name, email)
        else:
            print("Invalid type, defaulting to regular")
            user = RegularUser(name, email)

        users.append(user)

    return users

def add_transactions(users):
    for user in users:
        print(f"\nAdding transactions for {user.name}:")
        num_transactions = int(input("How many transactions? "))

        for _ in range(num_transactions):
            t_type = input("Transaction type (income/expense): ").strip().lower()
            amount = float(input("Amount: "))
            description = input("Description: ")

            if t_type == "income":
                user.wallet.add_transaction(Income(amount, description))
            elif t_type == "expense":
                user.wallet.add_transaction(Expense(amount, description))
            else:
                print("Invalid transaction type.")

def process_payments(users):
    for user in users:
        print(f"\nProcessing payments for {user.name}")
        num_payments = int(input("How many payments? "))

        for _ in range(num_payments):
            method = input("Payment method (upi/card/cash): ").strip().lower()
            amount = float(input("Amount: "))

            if method == "upi":
                UPI().pay(amount, user.wallet)
            elif method == "card":
                Card().pay(amount, user.wallet)
            elif method == "cash":
                Cash().pay(amount, user.wallet)
            else:
                print("Invalid payment method.")

        if hasattr(user, 'cashback'):
            apply_cashback = input("Apply cashback for premium user? (y/n): ")
            if apply_cashback == 'y':
                cashback_amount = float(input("Cashback base amount: "))
                user.cashback(cashback_amount)

def generate_reports(users):
    report = ConsoleReport()
    for user in users:
        print(f"\nReport for {user.name}:")
        report.generate(user.wallet)

def main():
    while True:
        print("""
======= EXPENSE MANAGER =======
1. Create User
2. Add Transaction
3. Make Payment
4. Apply Cashback (Premium)
5. Show Wallet Report
6. Exit
""")
        choice = input("Choose an option: ")

        if choice == "1":
            create_users()
        elif choice == "2":
            add_transactions()
        elif choice == "3":
            process_payments()
        elif choice == "4":
            generate_reports()
        elif choice == "5":
            print("Exiting application")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()