"""
Topic: Typing Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Define a `Literal` type alias `HTTPMethod = Literal["GET", "POST", "PUT", "DELETE"]`.
    """
    # TODO: Define Literal alias
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create a generic Stack class `Stack(Generic[T])` with methods `push(item: T)` and `pop() -> T`.
    """
    # TODO: Implement generic Stack
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Annotate a higher-order function `transform_elements(items: list[T], mapper: Callable[[T], R]) -> list[R]`.
    """
    # TODO: Implement typed mapper
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build a typed generic cache wrapper `CacheContainer[K, V]` with TTL and lookup stats.
    """
    # TODO: Implement CacheContainer[K, V]
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
