"""
Topic: Parameterized Decorator Factory Example
File: 02_examples.py
"""
from functools import wraps
from typing import Any, Callable

def repeat(num_times: int) -> Callable[..., Any]:
    """Decorator factory that accepts an argument specifying repeat count."""
    def decorator_repeat(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = None
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat


@repeat(num_times=3)
def send_ping(host: str) -> None:
    print(f"Ping sent to {host}")


if __name__ == "__main__":
    send_ping("127.0.0.1")
