"""
Solutions: Bytecode Exercises.
"""

from typing import Callable, Any


def get_function_variable_names(func: Callable[..., Any]) -> tuple[str, ...]:
    return func.__code__.co_varnames


if __name__ == "__main__":
    def example(x: int, y: int) -> int:
        z = x + y
        return z

    print("Variable names:", get_function_variable_names(example))
