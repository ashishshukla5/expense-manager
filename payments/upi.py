from payments.payment import PaymentMethod

class UPI(PaymentMethod):
    def pay(slef, amount):
        print(f"Paid {amount} using UPI")