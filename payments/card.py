from payments.payment import PaymentMethod

class Card(PaymentMethod):
    def pay(self, amount, wallet):
        if wallet.get_balance() >= amount:
            wallet._update_balance(-amount)
            print(f"Paid {amount} using Card")
        else:
            print("Insufficient balance for Card payment")