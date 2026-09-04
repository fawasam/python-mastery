"""
Topic: Variables & Dynamic Typing
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create 3 variables (product_name, unit_price, stock_quantity).
    Print them in a single readable sentence using f-strings or string formatting.
    """
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Given two variables `primary_color = 'Blue'` and `secondary_color = 'Red'`,
    swap their values using Python's idiomatic single-line unpacking technique.
    """
    primary_color = "Blue"
    secondary_color = "Red"
    # TODO: Swap primary_color and secondary_color
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Create a variable named `flexible_var`.
    Assign it an integer, print its `type()` and `id()`.
    Reassign it a list `[1, 2, 3]`, print its new `type()` and `id()`.
    """
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Define configuration variables for a database connection:
    - DB_HOST (string)
    - DB_PORT (int)
    - DB_USER (string)
    - IS_SSL_ENABLED (bool)
    Return a dictionary containing all 4 configuration values.
    """
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
