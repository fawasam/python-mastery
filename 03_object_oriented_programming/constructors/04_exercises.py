"""
Topic: Constructor Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a `Date` class with `year`, `month`, `day`. Implement a `@classmethod` `from_iso(iso_str)` parsing `"2026-09-04"`.
    """
    # TODO: Factory constructor from ISO string
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create a `User` model class with factory `@classmethod` `from_json(json_str)`.
    """
    # TODO: Factory constructor from JSON
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Implement a Singleton class `LoggerSingleton` using `__new__` that guarantees only 1 log handler instance exists.
    """
    # TODO: Singleton constructor
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an HTTP API response object class `ApiResponse` with factory classmethods `success(data)` and `error(message, status_code=400)`.
    """
    # TODO: Factory methods for API responses
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
