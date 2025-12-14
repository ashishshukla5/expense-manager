from wallet.wallet import Wallet

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.wallet = Wallet()

    def show_profile(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")