from payments.payment import PaymentMethod

class Card(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Card")