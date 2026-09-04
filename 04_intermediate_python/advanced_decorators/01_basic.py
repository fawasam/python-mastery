"""
Basic Parametrized and Class-Based Decorators in Python.
"""

import functools
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])


def repeat(times: int = 2) -> Callable[[F], F]:
    """
    Parametrized decorator factory that executes a function 'times' times.
    """

    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper  # type: ignore[return-value]

    return decorator


class CallCounter:
    """
    Class-based decorator that counts total invocations of the target function.
    """

    def __init__(self, func: Callable[..., Any]) -> None:
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.count += 1
        print(f"[METRIC] '{self.func.__name__}' called {self.count} time(s).")
        return self.func(*args, **kwargs)


@repeat(times=3)
def greet(name: str) -> None:
    print(f"Hello, {name}!")


@CallCounter
def process_task(task_name: str) -> str:
    return f"Completed {task_name}"


if __name__ == "__main__":
    print("--- Executing @repeat(times=3) ---")
    greet("Alice")

    print("\n--- Executing Class Decorator @CallCounter ---")
    process_task("Import Data")
    process_task("Export Report")
    print(f"Total recorded calls: {process_task.count}")
