"""
Topic: Conditionals Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Write a ternary expression that assigns `"even"` if `num` is divisible by 2, otherwise `"odd"`.
    """
    num = 7
    # TODO: Ternary expression
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Given a year integer (e.g. `2024`), determine if it is a leap year.
    Rule: Divisible by 4, except if divisible by 100 unless also divisible by 400.
    """
    year = 2024
    # TODO: Implement leap year check
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Implement a tax rate calculator function `get_tax_rate(income)`:
    - Income <= $10,000 -> 0% tax
    - $10,001 to $50,000 -> 10% tax
    - $50,001 to $100,000 -> 20% tax
    - Above $100,000 -> 30% tax
    """
    # TODO: Return tax rate float
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an HTTP response router function `route_status_code(code: int)` using clean guard clauses:
    - 200..299 -> "SUCCESS"
    - 400..499 -> "CLIENT_ERROR"
    - 500..599 -> "SERVER_ERROR"
    - Any other -> "UNKNOWN_STATUS"
    """
    # TODO: Route status code
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
