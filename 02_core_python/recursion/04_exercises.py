"""
Topic: Recursion Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Write a recursive function `recursive_sum(n: int) -> int` calculating sum of 1 to n.
    """
    # TODO: Recursive sum
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Write a recursive function `reverse_string(s: str) -> str`.
    """
    # TODO: Recursive reverse string
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Write a recursive function `flatten_nested_list(nested: list) -> list` that flattens arbitrary nested lists like `[1, [2, [3, 4], 5], 6]`.
    """
    # TODO: Flatten nested list
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build a recursive file finder function `find_files_by_extension(dir_path: Path, ext: str)` traversing directories recursively without `Path.rglob()`.
    """
    # TODO: Implement recursive directory crawler
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
