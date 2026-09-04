"""
Solution for Python Internals Exercises.
"""

from typing import Any, Callable


def get_function_constants(func: Callable[..., Any]) -> tuple[Any, ...]:
    return func.__code__.co_consts


def example_function(x: int) -> int:
    multiplier = 42
    msg = "Hello World"
    return x * multiplier


if __name__ == "__main__":
    consts = get_function_constants(example_function)
    print(f"Extracted function constants (co_consts): {consts}")
