from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount, wallet):
        """Process payment and deduct amount rom wallet"""
        pass