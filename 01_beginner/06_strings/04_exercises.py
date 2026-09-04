"""
Topic: String Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Given string `text = "python programming"`, capitalize the first letter of each word.
    """
    text = "python programming"
    # TODO: Capitalize each word
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Write a function `is_palindrome(s)` that returns True if string `s` reads the same forwards and backwards (case-insensitive, ignoring spaces).
    """
    # TODO: Check if string is palindrome
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Extract domain name from email string (e.g., `"john.doe@company.org"` -> `"company.org"`).
    Handle cases with leading/trailing whitespace.
    """
    # TODO: Extract domain
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Sanitize and mask user sensitive data (e.g. Credit Card number `"4532 8901 2345 9812"` -> `"XXXX-XXXX-XXXX-9812"`).
    """
    # TODO: Mask credit card string
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
