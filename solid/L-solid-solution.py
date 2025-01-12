from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self,balance:float):
        self.balance = balance

    def pay(self,amount:float):
        if amount > self.balance:
            raise ValueError("Not enough balance.")
        self.balance -= amount
        print(f"[PaymentMethod] Paid {amount}. New balance: {self.balance}")

class Refundable(PaymentMethod): # Refundable is abstract class
    @abstractmethod
    def refund(self,amount:float):
        pass

class CreditCard(Refundable):
    def refund(self, amount: float):
        self.balance += amount
        print(f"[CreditCard] Refunded {amount}. New balance: {self.balance}")

class NonRefundableGiftCard(PaymentMethod):
    pass