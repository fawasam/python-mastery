"""
Topic: Iterator Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create an iterator from string `"PYTHON"` and print each character using `next()` inside a `while True` loop catching `StopIteration`.
    """
    # TODO: Manual iteration
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create a custom iterator class `EvenNumbers(max_val: int)` yielding even numbers from 0 up to max_val.
    """
    # TODO: Custom iterator class
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Implement a custom bidirectional cycle iterator `CycleIterator(items: list)` that cycles through list items infinitely.
    """
    # TODO: Cycle iterator
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build a memory-safe batch/chunk iterator class `BatchIterator(data_list, batch_size)` yielding chunked lists of size batch_size.
    """
    # TODO: Batch iterator class
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
