"""
Advanced Decorators: Class-Based Call Counter Decorator.
"""

from functools import wraps
from typing import Any, Callable, TypeVar

R = TypeVar("R")


class CallCounter:
    """Class-based decorator tracking total invocation count of a function."""
    def __init__(self, func: Callable[..., R]) -> None:
        self.func = func
        self.calls = 0
        wraps(func)(self)

    def __call__(self, *args: Any, **kwargs: Any) -> R:
        self.calls += 1
        return self.func(*args, **kwargs)


@CallCounter
def compute_square(x: int) -> int:
    return x * x


if __name__ == "__main__":
    compute_square(4)
    compute_square(5)
    print(f"Function '{compute_square.__name__}' invoked {compute_square.calls} times.")
