from abc import ABC, abstractmethod


class PaymentGatewayInterface(ABC):
    @abstractmethod
    def charge(self, amount, payment_details):
        pass


class CreditCardPaymentGateway(PaymentGatewayInterface):
    def charge(self, amount, payment_details):
        return f"Charging {amount * 0.03} using credit card"


class PayPalPaymentGateway(PaymentGatewayInterface):
    def charge(self, amount, payment_details):
        return f"Charging {amount * 0.05} using PayPal"


class BankTransferPaymentGateway(PaymentGatewayInterface):
    def charge(self, amount, payment_details):
        return f"Charging {amount * 2.50} using bank transfer"


class CryptoPaymentGateway(PaymentGatewayInterface):
    def charge(self, amount, payment_details):
        return f"Charging {amount} using crypto"


class WireTransferPaymentGateway(PaymentGatewayInterface):
    def charge(self, amount, payment_details):
        return f"Charging {amount} using wire transfer"


class FeeCalculator:
    def __init__(self, payment_gateway: PaymentGatewayInterface):
        self.payment_gateway = payment_gateway

    def calculate_fee(self, amount):
        return self.payment_gateway.charge(amount, "payment details")


fee_calculator = FeeCalculator(CreditCardPaymentGateway())
