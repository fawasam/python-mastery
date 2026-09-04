"""
Topic: Type Hints Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Annotate function `multiply(a: float, b: float) -> float`.
    """
    # TODO: Add annotations
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Annotate function `parse_id(val: int | str) -> int`.
    """
    # TODO: Add union annotations
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Annotate function `transform_matrix(matrix: list[list[int]]) -> list[int]`.
    """
    # TODO: Add 2D matrix annotations
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Annotate complex API config loader function `load_config(env: str, overrides: dict[str, str | int] | None = None) -> dict[str, Any]`.
    """
    # TODO: Add complex config annotations
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
