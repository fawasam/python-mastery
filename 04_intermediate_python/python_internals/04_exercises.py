"""
Python Internals Exercises.
"""

from typing import Any, Callable


# Exercise 1 (Medium): Inspecting Function Constants
# Write a function get_function_constants(func) that returns a tuple of co_consts
# from the function's code object.
def get_function_constants(func: Callable[..., Any]) -> tuple[Any, ...]:
    raise NotImplementedError("Implement get_function_constants")
