"""
Topic: Property Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a `Rectangle(w, h)` class with computed property `area` returning `w * h`.
    """
    # TODO: Implement area property
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create an `Employee` class with property `salary`. Setter raises ValueError if `salary < 30000`.
    """
    # TODO: Implement salary property validator
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Create a `Temperature` class with `@property` `celsius` and computed property `fahrenheit` with a setter converting F to C internally.
    """
    # TODO: Implement dual temperature properties
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build a `CachedAPIResponse` class with computed property `is_expired` returning True if `(now - fetched_at) > ttl`.
    """
    # TODO: Implement CachedAPIResponse with expiration property
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
