"""
Invariants vs Validation: Distinguishing Invariants from Runtime Validation.
"""


def process_user_input(raw_age: str) -> int:
    """
    Public API endpoint: MUST use explicit ValueError/TypeError for data validation.
    """
    try:
        age = int(raw_age)
    except ValueError:
        raise ValueError(f"Age must be a valid integer string, got '{raw_age}'")

    if age < 0:
        raise ValueError("Age cannot be negative")

    return age


def internal_pension_calculator(validated_age: int) -> float:
    """
    Internal module helper: uses assertions to verify caller satisfied contract preconditions.
    """
    assert validated_age >= 0, "Precondition failed: validated_age cannot be negative"
    return max(0.0, (65 - validated_age) * 1000.0)


if __name__ == "__main__":
    age = process_user_input("45")
    pension = internal_pension_calculator(age)
    print(f"Calculated Pension: ${pension:.2f}")
