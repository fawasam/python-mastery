"""
Solutions for Lock Exercises.
"""

import threading


class ThreadSafeSet:
    def __init__(self) -> None:
        self._set: set[str] = set()
        self._lock = threading.Lock()

    def add(self, item: str) -> None:
        with self._lock:
            self._set.add(item)

    def contains(self, item: str) -> bool:
        with self._lock:
            return item in self._set


if __name__ == "__main__":
    ts = ThreadSafeSet()

    def worker(val: str):
        ts.add(val)

    threads = [threading.Thread(target=worker, args=(f"item_{i}",)) for i in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    assert ts.contains("item_5") is True
    print("Thread-safe set exercise passed successfully!")
