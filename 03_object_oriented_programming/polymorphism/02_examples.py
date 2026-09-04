"""
Topic: Polymorphic Payment Gateway Strategy
File: 02_examples.py
"""

class StripeGateway:
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} via Stripe API"


class PayPalGateway:
    def pay(self, amount: float) -> str:
        return f"Paid ${amount:.2f} via PayPal Express"


def checkout(gateway: Any, amount: float) -> None:
    receipt = gateway.pay(amount)
    print(receipt)


if __name__ == "__main__":
    checkout(StripeGateway(), 99.99)
    checkout(PayPalGateway(), 49.50)
