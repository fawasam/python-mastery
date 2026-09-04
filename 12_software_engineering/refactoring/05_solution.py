"""
Solutions: Refactoring Exercises.
"""

DISCOUNT_RATES: dict[str, float] = {
    "MEMBER": 0.05,
    "PREMIUM": 0.15,
}


def dirty_discount_calculator(user_type: str, total: float) -> float:
    """
    Refactored using dictionary strategy lookup.
    """
    discount_rate = DISCOUNT_RATES.get(user_type.upper(), 0.0)
    return total * (1.0 - discount_rate)


if __name__ == "__main__":
    print("Refactored discount (PREMIUM):", dirty_discount_calculator("PREMIUM", 100.0))
    print("Refactored discount (GUEST):", dirty_discount_calculator("GUEST", 100.0))
