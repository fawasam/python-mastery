"""
Closure Exercises.
"""

from typing import Callable


# Exercise 1 (Medium): Rate Limiter Closure
# Create a function make_rate_limiter(max_calls: int) that returns a closure.
# The closure takes no arguments. It increments a call count on each execution.
# If call count <= max_calls, return True. Otherwise, return False.
def make_rate_limiter(max_calls: int) -> Callable[[], bool]:
    raise NotImplementedError("Implement make_rate_limiter")


# Exercise 2 (Hard): History Function Factory
# Create a function make_history_tracker() that returns a tuple of two functions:
# (add_item, get_history).
# 'add_item(x)' adds x to an internal captured list.
# 'get_history()' returns a copy of the list.
def make_history_tracker() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    raise NotImplementedError("Implement make_history_tracker")
