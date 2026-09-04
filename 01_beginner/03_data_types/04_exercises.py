"""
Topic: Data Types Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Convert string `"49.99"` to a float, multiply it by `2`, and print the result.
    """
    price_str = "49.99"
    # TODO: Convert price_str to float and multiply by 2
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Write a function `is_truthy(val)` that prints whether `val` evaluates to True or False in Python.
    """
    # TODO: Implement truthiness printer
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Safely convert a string `input_val` to an integer.
    If conversion is successful, return the integer.
    If it fails, return `None`.
    """
    # TODO: Handle conversion safely without crashing
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Parse raw string data from an API payload:
    `payload = {"id": "101", "score": "98.5", "active": "True"}`
    Return a new dictionary where `id` is int, `score` is float, and `active` is bool.
    """
    # TODO: Cast payload values to appropriate primitive types
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
