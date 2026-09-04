"""
Topic: Callable Annotations Example
File: 02_examples.py
"""
from typing import Callable

def retry(operation: Callable[[], bool], retries: int = 3) -> bool:
    for attempt in range(1, retries + 1):
        if operation():
            print(f"Operation succeeded on attempt {attempt}")
            return True
        print(f"Attempt {attempt} failed.")
    return False


if __name__ == "__main__":
    count = 0
    def flaky() -> bool:
        global count
        count += 1
        return count >= 2

    retry(flaky)
