"""
Topic: Unpacking Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Unpack list `[10, 20, 30, 40, 50]` so that `first` is 10, `last` is 50, and `middle` is `[20, 30, 40]`.
    """
    # TODO: Unpack list
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Combine 3 dictionaries `d1 = {"a": 1}`, `d2 = {"b": 2}`, `d3 = {"c": 3}` into a single merged dictionary using unpacking.
    """
    # TODO: Merge 3 dicts
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Given a list of nested record tuples `[("Alice", (90, 85, 95)), ("Bob", (70, 80, 75))]`,
    unpack student name and individual grades directly in a loop header.
    """
    # TODO: Nested tuple unpacking in loop header
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Implement a function `build_config(*base_configs, **override_kwargs)` that merges multiple base config dictionaries sequentially, then applies final override kwargs.
    """
    # TODO: Implement dynamic config builder
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
