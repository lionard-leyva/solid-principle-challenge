from abc import ABC, abstractmethod

class IPaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class RefundServiceInterface(ABC):
    @abstractmethod
    def refund(self, amount: float) -> None:
        pass

class HandleDisputeInterface(ABC):
    @abstractmethod
    def handle_dispute(self, dispute_id: str) -> None:
        pass

class BasicGiftCard(IPaymentGateway):
    def pay(self, amount: float) -> None:
        print(f"Gift card used to pay {amount}.")

class CreditCard(IPaymentGateway, RefundServiceInterface):
    def pay(self, amount: float) -> None:
        print(f"Credit card used to pay {amount}.")

    def refund(self, amount: float) -> None:
        print(f"Credit card refunded {amount}.")