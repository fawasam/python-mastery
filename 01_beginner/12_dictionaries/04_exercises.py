"""
Topic: Dictionary Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a dictionary `inventory = {"apples": 50, "bananas": 30}`.
    Add `"oranges": 40` and update `"bananas"` to `45`.
    """
    # TODO: Update dictionary
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Given a sentence string `"apple banana apple cherry banana apple"`,
    build a word frequency counter dictionary `{"apple": 3, "banana": 2, "cherry": 1}`.
    """
    # TODO: Count word frequencies
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Invert a dictionary `mapping = {"a": 1, "b": 2, "c": 1}` into `inverted = {1: ["a", "c"], 2: ["b"]}`.
    """
    # TODO: Invert dictionary mapping
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Merge two application configuration dictionaries `default_config` and `user_override` recursively.
    `user_override` settings take precedence over `default_config`.
    """
    # TODO: Implement deep dictionary merge
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
