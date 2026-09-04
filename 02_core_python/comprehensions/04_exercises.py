"""
Topic: Comprehension Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Using list comprehension, generate cubes ($x^3$) of numbers 1 through 10.
    """
    # TODO: List comprehension of cubes
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Given a list of words `["apple", "banana", "apricot", "cherry", "avocado"]`,
    build a dict mapping each word starting with `"a"` to its length.
    """
    # TODO: Dict comprehension
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Given a 2D matrix `[[1, 2], [3, 4], [5, 6]]`, transpose it to `[[1, 3, 5], [2, 4, 6]]` using a nested list comprehension.
    """
    # TODO: Matrix transposition
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Filter and transform API user data: extract active user emails converted to lowercase from a list of user dicts.
    """
    # TODO: Extract active user emails
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
