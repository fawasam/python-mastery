"""
Topic: Magic Method Solutions
File: 05_solution.py
"""

class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self.x - other.x, self.y - other.y)

    def __repr__(self) -> str:
        return f"Vector2D({self.x}, {self.y})"


class Money:
    def __init__(self, amount: float, currency: str = "USD") -> None:
        self.amount = amount
        self.currency = currency

    def __add__(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError(f"Cannot add {self.currency} and {other.currency}")
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    def __repr__(self) -> str:
        return f"{self.currency} {self.amount:.2f}"


if __name__ == "__main__":
    print("--- Level 1 ---")
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)
    print(f"{v1} + {v2} = {v1 + v2}")

    print("\n--- Level 2 ---")
    m1 = Money(100.0, "USD")
    m2 = Money(50.0, "USD")
    print(f"{m1} + {m2} = {m1 + m2}")
