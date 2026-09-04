"""
Topic: Functional Programming Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Use `functools.partial` to create a `b64_encode` function pre-configured from a base encoding function.
    """
    # TODO: Create partial function
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Implement currying for a 3-argument function `add3(a)(b)(c)`.
    """
    # TODO: Implement currying
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Write a pure function `update_dict_immutable(d: dict, key: str, val: Any) -> dict` returning a new updated dict without mutating original `d`.
    """
    # TODO: Implement immutable dict updater
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build a data transformation pipeline using function composition `compose_pipeline(*funcs)`.
    """
    # TODO: Functional pipeline composition
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
