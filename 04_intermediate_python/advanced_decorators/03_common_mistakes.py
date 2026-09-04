"""
Common Mistakes in Advanced Decorators.
"""

import functools
from typing import Any, Callable


# MISTAKE 1: Forgetting @functools.wraps
def bad_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Wrapper docstring."""
        return func(*args, **kwargs)

    return wrapper  # Missing @functools.wraps(func)!


# GOOD PRACTICE: Always use @functools.wraps
def good_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """Wrapper docstring."""
        return func(*args, **kwargs)

    return wrapper


@bad_decorator
def target_a() -> None:
    """Original target_a docstring."""
    pass


@good_decorator
def target_b() -> None:
    """Original target_b docstring."""
    pass


if __name__ == "__main__":
    print("--- Introspection with bad_decorator (Missing @wraps) ---")
    print(f"Name: {target_a.__name__}")  # Output: wrapper (LOST original name!)
    print(f"Docstring: {target_a.__doc__}")  # Output: Wrapper docstring.

    print("\n--- Introspection with good_decorator (Uses @wraps) ---")
    print(f"Name: {target_b.__name__}")  # Output: target_b (PRESERVED!)
    print(f"Docstring: {target_b.__doc__}")  # Output: Original target_b docstring.
