from payments.payment import PaymentMethod

class UPI(PaymentMethod):
    def pay(slef, amount, wallet):
        if wallet.get_balance() >= amount:
            wallet._update_balance(-amount)
            print(f"Paid {amount} using UPI")
        else:
            print("Insufficient balance for UPI payment")