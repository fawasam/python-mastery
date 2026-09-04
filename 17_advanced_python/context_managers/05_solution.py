"""
Solutions: Context Managers Exercises.
"""

from typing import Any


class DummyContextManager:
    def __enter__(self) -> "DummyContextManager":
        print("ENTER")
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        print("EXIT")


if __name__ == "__main__":
    with DummyContextManager():
        print("INSIDE")
