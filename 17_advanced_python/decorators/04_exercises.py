"""
Exercises: Custom Decorator Implementation.
"""

from typing import Callable, Any, TypeVar

R = TypeVar("R")


def uppercase_string_result(func: Callable[..., str]) -> Callable[..., str]:
    """
    Exercise: Write decorator that converts the string return value of func to uppercase.
    
    Level 1 - Easy
    """
    raise NotImplementedError("Implement uppercase_string_result")
