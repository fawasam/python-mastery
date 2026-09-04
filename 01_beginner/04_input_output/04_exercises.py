"""
Topic: Input & Output Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Format a floating-point number `78.12945` to 2 decimal places using an f-string.
    """
    number = 78.12945
    # TODO: Format to 2 decimal places
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Format an integer `1250000` with commas as thousand separators.
    """
    population = 1250000
    # TODO: Format with commas
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Create a receipt line generator function `format_receipt_item(name, qty, unit_price)`.
    Format item name left-aligned (15 spaces), qty centered (5 spaces), and total right-aligned (10 spaces, 2 decimal places).
    """
    # TODO: Implement receipt line formatter
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Format a progress metrics dashboard string showing:
    - Cpu Usage: 74.2%
    - Memory Used: 12.45 GB / 16.00 GB
    - Total Requests: 1,450,200
    """
    # TODO: Generate dashboard report string
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
