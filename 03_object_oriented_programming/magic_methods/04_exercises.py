"""
Topic: Magic Method Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a `Vector2D(x, y)` class with `__add__`, `__sub__`, and `__repr__`.
    """
    # TODO: Implement Vector2D
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create a `Money(amount, currency)` class with `__add__` (raise ValueError if currencies mismatch) and `__eq__`.
    """
    # TODO: Implement Money operator overloading
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Implement a `Polynomial` class with `__add__` and `__call__(x)` allowing polynomial evaluation like `p(5)`.
    """
    # TODO: Implement Callable polynomial
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build a `PaginatedDataset` container class implementing `__len__`, `__getitem__`, and `__iter__` for chunked datasets.
    """
    # TODO: Implement PaginatedDataset container
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
