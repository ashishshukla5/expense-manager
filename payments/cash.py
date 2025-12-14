from payments.payment import PaymentMethod

class Cash(PaymentMethod):
    def pay(self, amount, wallet):
        if wallet.get_balance() >= amount:
            wallet._update_balance(-amount)
            print(f"Paid {amount} using Cash")
        else:
            print("Insufficient balance for ash payment")