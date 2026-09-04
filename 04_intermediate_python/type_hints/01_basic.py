"""
Topic: Modern Type Hints (Python 3.10+)
File: 01_basic.py
"""

def calculate_discount(price: float, discount_pct: float | None = None) -> float:
    if discount_pct is None:
        return price
    return price * (1.0 - discount_pct)


if __name__ == "__main__":
    p1 = calculate_discount(100.0)
    p2 = calculate_discount(100.0, 0.20)
    print(f"Price 1: ${p1:.2f} | Price 2: ${p2:.2f}")
