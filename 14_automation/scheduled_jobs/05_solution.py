"""
Solutions: Scheduled Jobs Exercises.
"""

from typing import Callable, Any


def execute_n_times(func: Callable[[], Any], n: int) -> list[Any]:
    results = []
    for _ in range(n):
        results.append(func())
    return results


if __name__ == "__main__":
    count = [0]
    def increment() -> int:
        count[0] += 1
        return count[0]

    res = execute_n_times(increment, 3)
    print("Execution results:", res)
