"""
Topic: Loop Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Calculate the sum of all integers from 1 to 50 using a `for` loop.
    """
    # TODO: Calculate sum 1..50
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Print the multiplication table for number `7` (from 7 x 1 to 7 x 10).
    """
    # TODO: Print multiplication table
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Find all prime numbers between 2 and 30 using nested `for-else` loops.
    """
    # TODO: Find primes
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Simulate a polling retry loop `retry_connection(max_attempts=5)`.
    Attempt connecting (simulate failure on attempts 1-3, success on attempt 4).
    If max_attempts is exceeded without success, log a timeout failure.
    """
    # TODO: Implement retry loop
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
