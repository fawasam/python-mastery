"""
Topic: JSON Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Serialize dictionary `{"app": "Mastery", "version": 1.0}` to a JSON string formatted with 4 spaces indentation.
    """
    # TODO: Serialize JSON with indent 4
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Safely parse JSON string `{"name": "Alice"}`. Handle `json.JSONDecodeError` if invalid string is passed.
    """
    # TODO: Safely parse JSON
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Implement a custom JSONEncoder that handles `Decimal` and `date` objects.
    """
    # TODO: Custom encoder for Decimal and date
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an atomic JSON file updating function `update_json_key(file_path: Path, key: str, value: Any)`.
    """
    # TODO: Atomic JSON config updater
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
