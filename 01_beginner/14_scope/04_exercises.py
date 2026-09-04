"""
Topic: Scope Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Demonstrate variable shadowing by creating a global variable `x = 10` and a function `foo()` with local `x = 20`.
    Print both values to prove the global x is unaffected.
    """
    # TODO: Demonstrate local vs global x
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Create a nested function closure `make_accumulator(initial_value=0)` that uses `nonlocal` to add values to a running total.
    """
    # TODO: Implement closure accumulator
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Fix an `UnboundLocalError` bug in a function attempting to update a global dictionary configuration without reassigning the variable reference.
    """
    # TODO: Handle global dictionary updates
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build a thread-safe / scope-safe rate limiter token bucket factory function using `nonlocal` state management.
    """
    # TODO: Implement token bucket rate limiter closure
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
