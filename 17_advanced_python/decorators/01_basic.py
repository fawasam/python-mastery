"""
Advanced Decorators Basics: Parameterized Decorator Factory with Retry Logic.
"""

from functools import wraps
import time
from typing import Callable, TypeVar

R = TypeVar("R")


def retry(max_attempts: int = 3, delay: float = 0.01) -> Callable[[Callable[..., R]], Callable[..., R]]:
    """Decorator factory retrying failing function invocations up to max_attempts times."""
    def decorator(func: Callable[..., R]) -> Callable[..., R]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> R:
            last_err = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    last_err = err
                    time.sleep(delay)
            raise RuntimeError(f"Function {func.__name__} failed after {max_attempts} attempts: {last_err}")
        return wrapper
    return decorator


attempts = [0]


@retry(max_attempts=3, delay=0.01)
def unstable_network_call() -> str:
    attempts[0] += 1
    if attempts[0] < 2:
        raise ConnectionResetError("Socket reset")
    return "SUCCESS"


if __name__ == "__main__":
    res = unstable_network_call()
    print(f"Call succeeded on attempt #{attempts[0]}: {res}")
