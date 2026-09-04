"""
Basic Design Patterns: Factory Method & Strategy Pattern in Python.
"""

from abc import ABC, abstractmethod


# ==========================================
# 1. Factory Method Pattern
# ==========================================

class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"[EMAIL] {message}")


class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"[SMS] {message}")


class NotificationFactory:
    """Factory creating notification instances based on channel type."""
    @staticmethod
    def create_notification(channel: str) -> Notification:
        if channel == "email":
            return EmailNotification()
        elif channel == "sms":
            return SMSNotification()
        raise ValueError(f"Unknown channel: {channel}")


# ==========================================
# 2. Strategy Pattern
# ==========================================

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass


class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str) -> None:
        self.card_number = card_number

    def pay(self, amount: float) -> None:
        print(f"Paid ${amount:.2f} using Credit Card ({self.card_number[-4:]})")


class PayPalPayment(PaymentStrategy):
    def __init__(self, email: str) -> None:
        self.email = email

    def pay(self, amount: float) -> None:
        print(f"Paid ${amount:.2f} using PayPal ({self.email})")


class ShoppingCart:
    """Context object configured with an interchangeable PaymentStrategy."""
    def __init__(self, payment_strategy: PaymentStrategy) -> None:
        self.payment_strategy = payment_strategy
        self.items: list[float] = []

    def add_item(self, price: float) -> None:
        self.items.append(price)

    def checkout(self) -> None:
        total = sum(self.items)
        self.payment_strategy.pay(total)


if __name__ == "__main__":
    # Factory Demo
    notif = NotificationFactory.create_notification("email")
    notif.send("Welcome to Design Patterns!")
    
    # Strategy Demo
    cart = ShoppingCart(PayPalPayment("user@example.com"))
    cart.add_item(49.99)
    cart.add_item(15.00)
    cart.checkout()
