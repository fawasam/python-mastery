"""
Topic: Module Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Use the `math` module to calculate the area of a circle with radius `7.5` ($A = \pi \cdot r^2$).
    """
    # TODO: Calculate circle area
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Use `random` module to simulate rolling two 6-sided dice 100 times. Count how many times the sum equals `7`.
    """
    # TODO: Simulate dice rolls
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Use `collections.Counter` to find the 3 most frequent letters in string `"abracadabra"`.
    """
    # TODO: Find top 3 letters
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Write a system diagnostic function using `sys` and `os` that prints Python version, platform OS name, and CPU count.
    """
    # TODO: Gather system metrics via standard library
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
