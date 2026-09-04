"""
Topic: Abstract Base Classes Basics
File: 01_basic.py
"""
from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        """Mandatory abstract method to process payment."""
        pass

    @abstractmethod
    def refund_payment(self, transaction_id: str) -> bool:
        """Mandatory abstract method to refund payment."""
        pass


class StripeProcessor(PaymentGateway):
    def process_payment(self, amount: float) -> bool:
        print(f"[Stripe] Charged ${amount:.2f}")
        return True

    def refund_payment(self, transaction_id: str) -> bool:
        print(f"[Stripe] Refunded transaction '{transaction_id}'")
        return True


if __name__ == "__main__":
    processor = StripeProcessor()
    processor.process_payment(100.0)
    processor.refund_payment("tx_9901")
