from abc import ABC, abstractmethod

class PaymentGatewayInterface(ABC):
    @abstractmethod
    def pay (self, amount: float) -> None:
        pass

class PaypalService(PaymentGatewayInterface):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Paypal.")

class YapeService(PaymentGatewayInterface):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Yape.")

class PaymentProcessor:
    def __init__(self, payment_gateway: PaymentGatewayInterface):
        self.payment_gateway = payment_gateway

    def process_payment(self, amount: float):
        self.payment_gateway.pay(amount)

paypal_service = PaymentProcessor(PaypalService())