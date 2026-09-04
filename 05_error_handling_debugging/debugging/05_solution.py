"""
Solutions for Debugging Exercises.
"""

from typing import Callable


def extract_error_line(func: Callable[[], None]) -> str:
    try:
        func()
        return "No Exception"
    except Exception as e:
        return f"{type(e).__name__}: {e}"


def faulty_target() -> None:
    _ = 1 / 0


if __name__ == "__main__":
    error_info = extract_error_line(faulty_target)
    print(f"Extracted Error Info: {error_info}")
