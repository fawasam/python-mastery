"""
Topic: Function Exercises
File: 04_exercises.py
"""

def level_1_easy() -> None:
    """
    Level 1 — Easy:
    Write a function `is_even(n: int) -> bool` that returns True if integer n is even, False otherwise.
    """
    # TODO: Implement is_even
    raise NotImplementedError("Level 1 exercise not completed yet.")


def level_2_medium() -> None:
    """
    Level 2 — Medium:
    Write a function `sum_numbers(*args: float) -> float` that accepts any number of numeric arguments and returns their sum.
    """
    # TODO: Implement sum_numbers using *args
    raise NotImplementedError("Level 2 exercise not completed yet.")


def level_3_hard() -> None:
    """
    Level 3 — Hard:
    Write a function `build_user_profile(username: str, **kwargs: str | int)` that returns a dictionary containing username and all kwargs formatted nicely.
    """
    # TODO: Implement build_user_profile using **kwargs
    raise NotImplementedError("Level 3 exercise not completed yet.")


def level_4_real_world() -> None:
    """
    Level 4 — Real World:
    Build a pipeline step wrapper `retry_pipeline_task(task_func, retries=3, *args, **kwargs)` that executes task_func(*args, **kwargs) and retries up to `retries` times if an exception occurs.
    """
    # TODO: Implement function decorator/wrapper pattern
    raise NotImplementedError("Level 4 exercise not completed yet.")


if __name__ == "__main__":
    print("--- Running Exercises ---")
    for lvl, fn in enumerate([level_1_easy, level_2_medium, level_3_hard, level_4_real_world], 1):
        try:
            fn()
        except NotImplementedError as e:
            print(f"Level {lvl}: {e}")
