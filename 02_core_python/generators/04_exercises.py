"""
Topic: Generator Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Write a generator function `even_generator(limit: int)` that yields even numbers from 0 up to limit.
    """
    # TODO: Implement even_generator
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create a generator expression that calculates the square root of all odd numbers in `range(1, 20)`.
    """
    # TODO: Generator expression
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Write an infinite generator `infinite_id_generator(prefix="usr_")` yielding `"usr_1"`, `"usr_2"`, `"usr_3"`, ... indefinitely.
    """
    # TODO: Infinite ID generator
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build a streaming CSV line generator `parse_csv_stream(file_lines)` that yields parsed dictionaries lazily without loading the entire CSV into memory.
    """
    # TODO: Streaming CSV parser
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
