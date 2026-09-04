"""
Topic: Function Solutions
File: 05_solution.py
"""
from typing import Any, Callable

def level_1_easy(n: int) -> bool:
    res = n % 2 == 0
    print(f"Is {n} even? {res}")
    return res


def level_2_medium(*args: float) -> float:
    total = sum(args)
    print(f"Sum of {args}: {total}")
    return total


def level_3_hard(username: str, **kwargs: Any) -> dict[str, Any]:
    profile = {"username": username, **kwargs}
    print("User Profile:", profile)
    return profile


def level_4_real_world(task_func: Callable[..., Any], retries: int = 3, *args: Any, **kwargs: Any) -> Any:
    for attempt in range(1, retries + 1):
        try:
            print(f"Executing task attempt {attempt}/{retries}...")
            return task_func(*args, **kwargs)
        except Exception as e:
            print(f"  Attempt {attempt} failed with error: {e}")
            if attempt == retries:
                raise e


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy(8)

    print("\n--- Level 2 ---")
    level_2_medium(10.5, 20.0, 5.5)

    print("\n--- Level 3 ---")
    level_3_hard("johndoe", role="Admin", department="DevOps", active=True)

    print("\n--- Level 4 ---")
    def flaky_task(x: int) -> int:
        if x < 10:
            raise ValueError("Input x must be >= 10")
        return x * 2

    try:
        level_4_real_world(flaky_task, retries=2, x=5)
    except ValueError:
        print("Pipeline task failed as expected after retries.")
