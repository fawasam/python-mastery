"""
Topic: Map, Filter & Reduce Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Use `map()` and `lambda` to convert temperatures in Celsius `[0, 20, 30, 40]` to Fahrenheit ($F = C \times 1.8 + 32$).
    """
    # TODO: Map Celsius to Fahrenheit
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Use `filter()` to extract prime numbers from list `range(2, 30)`.
    """
    # TODO: Filter primes
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Use `reduce()` to find the maximum number in a list `[14, 88, 42, 99, 12]` without using built-in `max()`.
    """
    # TODO: Implement max via reduce
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an event log aggregator function using `map`, `filter`, and `reduce` to sum response sizes for HTTP 200 responses.
    """
    # TODO: Implement log aggregator
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
