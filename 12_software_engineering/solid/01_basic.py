"""
SOLID Principles Part 1: SRP, OCP, and LSP in Python.
"""

from abc import ABC, abstractmethod


# ==========================================
# 1. Single Responsibility Principle (SRP)
# ==========================================

class User:
    """SRP: Holds user data only."""
    def __init__(self, email: str) -> None:
        self.email = email


class UserRepository:
    """SRP: Responsible ONLY for persisting user data."""
    def save(self, user: User) -> None:
        print(f"Saved {user.email} to database.")


class EmailNotifier:
    """SRP: Responsible ONLY for sending emails."""
    def send_welcome_email(self, user: User) -> None:
        print(f"Sent welcome email to {user.email}.")


# ==========================================
# 2. Open/Closed Principle (OCP)
# ==========================================

class DiscountStrategy(ABC):
    """OCP: Base abstraction open for extension via new strategies."""
    @abstractmethod
    def calculate(self, amount: float) -> float:
        pass


class RegularDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.05


class VIPDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.20


# Extension without modifying existing calculator logic
class BlackFridayDiscount(DiscountStrategy):
    def calculate(self, amount: float) -> float:
        return amount * 0.50


class DiscountCalculator:
    """OCP: Closed for modification. Accepts any DiscountStrategy."""
    def apply_discount(self, amount: float, strategy: DiscountStrategy) -> float:
        return amount - strategy.calculate(amount)


# ==========================================
# 3. Liskov Substitution Principle (LSP)
# ==========================================

class Bird(ABC):
    @abstractmethod
    def move(self) -> str:
        pass


class FlyingBird(Bird):
    def move(self) -> str:
        return "Flying high in the sky"


class Penguin(Bird):
    """LSP: Penguin is a Bird, but moves by waddling rather than flying."""
    def move(self) -> str:
        return "Waddling on ice"


def make_bird_move(bird: Bird) -> None:
    """LSP: Accepts any Bird subclass without breaking."""
    print(bird.move())


if __name__ == "__main__":
    # SRP
    u = User("alice@example.com")
    UserRepository().save(u)
    EmailNotifier().send_welcome_email(u)
    
    # OCP
    calc = DiscountCalculator()
    print("VIP Discount price:", calc.apply_discount(100.0, VIPDiscount()))
    print("Black Friday price:", calc.apply_discount(100.0, BlackFridayDiscount()))
    
    # LSP
    make_bird_move(FlyingBird())
    make_bird_move(Penguin())
