"""
Advanced Decorator Exercises.
"""

from typing import Any, Callable


# Exercise 1 (Medium): Parametrized Type Enforcer
# Implement @enforce_return_type(expected_type) that verifies the decorated function's return value.
# Raises TypeError if the return value does not match expected_type.
def enforce_return_type(expected_type: type) -> Callable[..., Any]:
    raise NotImplementedError("Implement enforce_return_type")


# Exercise 2 (Hard): Class Decorator add_timestamp
# Implement a class decorator @add_timestamp that adds a 'created_at' attribute (ISO format string)
# to every instance created from the decorated class.
def add_timestamp(cls: type) -> type:
    raise NotImplementedError("Implement add_timestamp")
