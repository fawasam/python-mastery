"""
Topic: Exception Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Write a function `safe_int_cast(val: str) -> int` that returns 0 if val cannot be cast to an integer.
    """
    # TODO: Handle ValueError cleanly
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Safely access dictionary key `lookup_dict_key(d: dict, key: str, default: Any)` using a try-except block catching KeyError.
    """
    # TODO: Catch KeyError
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Write a function `process_list_element(items: list, index: int)` handling IndexError and TypeError separately.
    """
    # TODO: Handle multiple exception types
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an API payload extractor function `extract_user_id(payload: dict)`.
    Raise a descriptive ValueError("Missing 'user' object in payload") if missing keys occur.
    """
    # TODO: Implement exception raising for validation
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
