from payments.payment import PaymentMethod

class Cash(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Cash")