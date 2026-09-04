"""
Common SOLID Violations in Python Codebases.
"""

from typing import Any


class BadPaymentProcessor:
    """
    VIOLATION OF OCP (Open/Closed Principle):
    Modifying this method is required every time a new payment method is added.
    """
    def process(self, payment_type: str, amount: float) -> None:
        if payment_type == "credit_card":
            print(f"Charging ${amount} via Credit Card")
        elif payment_type == "paypal":
            print(f"Charging ${amount} via PayPal")
        elif payment_type == "crypto":  # Added new payment type by modifying existing code!
            print(f"Charging ${amount} via Crypto")
        else:
            raise ValueError("Unsupported payment type")


class BadOrderService:
    """
    VIOLATION OF DIP (Dependency Inversion Principle):
    Directly instantiates concrete database inside constructor. Impossible to unit test.
    """
    def __init__(self) -> None:
        # Bad: tightly coupled to concrete PostgresDatabase
        self.db: Any = "Concrete Postgres Instance"


if __name__ == "__main__":
    p = BadPaymentProcessor()
    p.process("credit_card", 50.0)
