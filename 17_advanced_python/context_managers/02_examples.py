"""
Advanced Context Managers: Class-based exception suppression.
"""

from typing import Any, Type


class SuppressExceptions:
    """Context manager suppressing specified exception types."""
    def __init__(self, *exceptions: Type[BaseException]) -> None:
        self.exceptions = exceptions

    def __enter__(self) -> "SuppressExceptions":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool:
        # Returning True suppresses exception propagation
        if exc_type is not None and issubclass(exc_type, self.exceptions):
            print(f"[Suppressed exception]: {exc_val}")
            return True
        return False


if __name__ == "__main__":
    with SuppressExceptions(KeyError, ValueError):
        print("Inside block before error...")
        raise KeyError("Missing dictionary key")
    print("Execution continued safely past suppressed exception block.")
