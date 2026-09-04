"""
Topic: Method Types Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a `TemperatureConverter` class with `@staticmethod` `celsius_to_fahrenheit(c: float) -> float`.
    """
    # TODO: Create static method
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create a `Counter` class with class attribute `total_count = 0`. Add `@classmethod` `increment()` to increase total_count.
    """
    # TODO: Create classmethod counter
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Create a `StringUtil` class with static methods `clean_whitespace(s)`, `capitalize_words(s)`, and `to_slug(s)`.
    """
    # TODO: Implement static utility class
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build a `PaymentProcessor` class with instance method `process_payment(amt)`, class method `get_supported_currencies()`, and static method `format_currency(amt, currency)`.
    """
    # TODO: Implement PaymentProcessor
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
