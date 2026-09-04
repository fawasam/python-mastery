"""
Topic: List Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a list `nums = [10, 20, 30, 40, 50]`. Remove `30` and add `35` at index 2.
    """
    # TODO: Modify list
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Given a list with duplicate elements `[1, 2, 2, 3, 4, 4, 5]`,
    return a new list with unique elements preserving original order.
    """
    # TODO: Deduplicate preserving order
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Sort a list of tuples `students = [("Alice", 88), ("Bob", 95), ("Charlie", 78)]` by grade descending.
    """
    # TODO: Sort by grade descending
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Implement a sliding window average generator function `moving_average(data: list[float], window_size: int) -> list[float]`.
    """
    # TODO: Calculate moving average list
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
