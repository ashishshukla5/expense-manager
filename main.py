from users.regular_user import RegularUser
from users.premium_user import PremiumUser
from wallet.transaction import Income, Expense
from payments.upi import UPI
from payments.card import Card
from payments.cash import Cash
from reports.console_report import ConsoleReport

def main():
    user1 = RegularUser("Ashish", "ashish@gmail.com")
    user2 = PremiumUser("Rahul", "rahul@gmail.com")

    user1.wallet.add_transaction(Income(5000, "Salary"))
    user2.wallet.add_transaction(Income(10000, "Salary"))

    user1.wallet.add_transaction(Expense(1200, "Food"))
    user2.wallet.add_transaction(Expense(2000, "Shopping"))

    user2.cashback(10000)

    payments = [UPI(), Card(), Cash()]
    for payment in payments:
        print(f"\nProcessing payments for {user1.name}:")
        payment.pay(500)

    report = ConsoleReport()
    print(f"\nReport for {user1.name}:")
    report.generate(user1.wallet)

    print(f"Report for {user2.name}:")
    report.generate(user2.wallet)


if __name__ == "__main__":
    main()