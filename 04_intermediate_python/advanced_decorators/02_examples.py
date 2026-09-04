"""
Advanced Decorator Examples: Parametrized Retry Mechanism with Backoff and Class Decorators.
"""

import functools
import time
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def retry(max_attempts: int = 3, delay: float = 0.1) -> Callable[[F], F]:
    """
    Decorator that retries execution upon failure up to max_attempts times.
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    print(f"[RETRY] Attempt {attempt}/{max_attempts} failed for '{func.__name__}': {e}")
                    if attempt < max_attempts:
                        time.sleep(delay)
            raise last_exception  # type: ignore[misc]

        return wrapper  # type: ignore[return-value]

    return decorator


def singleton(cls: type) -> Callable[..., Any]:
    """
    Class decorator ensuring only a single instance of the decorated class ever exists.
    """
    instances: dict[type, Any] = {}

    @functools.wraps(cls)
    def get_instance(*args: Any, **kwargs: Any) -> Any:
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@retry(max_attempts=3, delay=0.05)
def unstable_network_call(success_on_attempt: int, current_state: dict[str, int]) -> str:
    current_state["attempt"] += 1
    if current_state["attempt"] < success_on_attempt:
        raise ConnectionError("Network timeout!")
    return "200 OK: Data retrieved"


@singleton
class DatabasePool:
    def __init__(self) -> None:
        self.connection_id = "CONN-1001"


if __name__ == "__main__":
    print("--- Testing Retry Decorator ---")
    state = {"attempt": 0}
    result = unstable_network_call(2, state)
    print(f"Network call result: {result}")

    print("\n--- Testing Singleton Class Decorator ---")
    db1 = DatabasePool()
    db2 = DatabasePool()
    print(f"db1 connection ID: {db1.connection_id}")
    print(f"db1 is db2: {db1 is db2} (Single instance confirmed!)")
