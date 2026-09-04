"""
Topic: Tuple Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a tuple storing your birth year, month, and day. Unpack them into separate variables.
    """
    # TODO: Create and unpack tuple
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Given a list of numbers `[1, 2, 3, 4, 5, 6]`, use extended unpacking to assign `first`, `last`, and `middle` numbers.
    """
    # TODO: Unpack using * operator
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Write a function `min_max_avg(numbers: list[float]) -> tuple[float, float, float]` returning minimum, maximum, and average.
    """
    # TODO: Return tuple containing min, max, avg
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Implement an immutable configuration loader that returns a named tuple or tuple of database setting records.
    """
    # TODO: Implement immutable configuration handler
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
