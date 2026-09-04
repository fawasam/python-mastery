"""
Solutions for Advanced Decorator Exercises.
"""

from datetime import datetime, timezone
import functools
from typing import Any, Callable


def enforce_return_type(expected_type: type) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = func(*args, **kwargs)
            if not isinstance(result, expected_type):
                raise TypeError(f"Function '{func.__name__}' returned {type(result).__name__}, expected {expected_type.__name__}")
            return result

        return wrapper

    return decorator


def add_timestamp(cls: type) -> type:
    original_init = cls.__init__

    @functools.wraps(original_init)
    def new_init(self: Any, *args: Any, **kwargs: Any) -> None:
        original_init(self, *args, **kwargs)
        self.created_at = datetime.now(timezone.utc).isoformat()

    cls.__init__ = new_init  # type: ignore[assignment]
    return cls


@enforce_return_type(int)
def calculate_area(width: int, height: int) -> int:
    return width * height


@add_timestamp
class UserAccount:
    def __init__(self, username: str) -> None:
        self.username = username


if __name__ == "__main__":
    area = calculate_area(5, 10)
    print(f"Calculated Area (int): {area}")

    user = UserAccount("johndoe")
    print(f"User: {user.username}, Created At: {user.created_at}")
