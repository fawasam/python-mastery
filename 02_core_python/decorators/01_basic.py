"""
Topic: Decorator Fundamentals & @wraps
File: 01_basic.py
"""
import time
from functools import wraps
from typing import Any, Callable

def timer_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that measures and prints execution time of a function."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start_time) * 1000
        print(f"⏱️ [{func.__name__}] Executed in {elapsed:.3f} ms")
        return result
    return wrapper


@timer_decorator
def compute_heavy_sum(limit: int) -> int:
    """Calculates the sum of numbers from 1 to limit."""
    return sum(range(1, limit + 1))


if __name__ == "__main__":
    res = compute_heavy_sum(1_000_000)
    print(f"Result: {res}")
    print(f"Function Name preserved by @wraps: {compute_heavy_sum.__name__}")
