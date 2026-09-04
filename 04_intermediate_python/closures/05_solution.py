"""
Solutions for Closure Exercises.
"""

from typing import Callable


def make_rate_limiter(max_calls: int) -> Callable[[], bool]:
    calls = 0

    def allow_request() -> bool:
        nonlocal calls
        if calls < max_calls:
            calls += 1
            return True
        return False

    return allow_request


def make_history_tracker() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    history: list[str] = []

    def add_item(item: str) -> None:
        history.append(item)

    def get_history() -> list[str]:
        return history.copy()  # Return a copy to preserve encapsulate state

    return add_item, get_history


if __name__ == "__main__":
    limiter = make_rate_limiter(2)
    print(f"Call 1 allowed: {limiter()}")  # True
    print(f"Call 2 allowed: {limiter()}")  # True
    print(f"Call 3 allowed: {limiter()}")  # False (Exceeded rate limit!)

    add_log, view_log = make_history_tracker()
    add_log("User logged in")
    add_log("User changed password")
    print(f"Audit History: {view_log()}")
