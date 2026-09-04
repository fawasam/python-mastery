"""
Solutions: Decorator Exercises.
"""

from functools import wraps
from typing import Callable, Any


def uppercase_string_result(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> str:
        res = func(*args, **kwargs)
        return res.upper()
    return wrapper


@uppercase_string_result
def greet(name: str) -> str:
    return f"hello, {name}"


if __name__ == "__main__":
    print("Decorated greeting:", greet("world"))
