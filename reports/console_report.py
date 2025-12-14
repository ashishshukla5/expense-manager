from reports.report import Report

class ConsoleReport(Report):
    def generate(self, wallet):
        print("\n--- Wallet Report ---")
        print(f"Balance: {wallet.get_balance()}")
        income_total = sum(t.amount for t in wallet.transactions if t.__class__.__name__ == "Income")
        expense_total = sum(t.amount for t in wallet.transactions if t.__class__.__name__ == "Expense")
        print(f"Total Income: {income_total}")
        print(f"Total Expenses: {expense_total}")
        print("\nTransactions:")
        for t in wallet.transactions:
            print(f"{t.__class__.__name__}: {t.amount} - {getattr(t, 'description', 'No desc')}")
        print("--------------------\n")