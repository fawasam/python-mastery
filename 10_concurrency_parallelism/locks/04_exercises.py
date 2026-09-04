"""
Lock Exercises.
"""

import threading


class ThreadSafeSet:
    def __init__(self) -> None:
        self._set: set[str] = set()
        self._lock = threading.Lock()

    def add(self, item: str) -> None:
        raise NotImplementedError("Implement thread-safe add using self._lock")

    def contains(self, item: str) -> bool:
        raise NotImplementedError("Implement thread-safe contains using self._lock")
