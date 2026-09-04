"""
Exercises: Building Custom Context Managers.
"""

from typing import Any


class DummyContextManager:
    """
    Exercise: Implement class-based context manager printing 'ENTER' on enter and 'EXIT' on exit.
    
    Level 1 - Easy
    """
    def __enter__(self) -> "DummyContextManager":
        raise NotImplementedError

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        raise NotImplementedError
