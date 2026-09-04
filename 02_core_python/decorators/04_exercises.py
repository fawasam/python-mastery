"""
Topic: Decorator Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Create a `@log_calls` decorator that prints `"Calling <function_name>"` before executing the decorated function.
    """
    # TODO: Create @log_calls
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create a `@validate_positive` decorator that raises ValueError if any numeric argument passed to the function is negative.
    """
    # TODO: Create input validation decorator
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Implement an in-memory `@memoize` caching decorator that stores return values of pure functions by argument key tuple.
    """
    # TODO: Create memoize decorator
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build an `@require_role(role="ADMIN")` authorization decorator factory for backend endpoints.
    """
    # TODO: Implement RBAC authorization decorator
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
