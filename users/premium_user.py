from users.user import User

class PremiumUser(User):
    def user_type(self):
        return "Premium"
    
    def cashback(self, amount):
        if amount <= 0:
            print("Invalid amount for cashback")
            return
        
        cashback_amount = amount * 0.05
        self.wallet._update_balance(cashback_amount)
        print(f"Cashback added: {cashback_amount}")