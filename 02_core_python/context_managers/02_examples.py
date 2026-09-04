"""
Topic: contextlib.contextmanager Decorator
File: 02_examples.py
"""
import time
from contextlib import contextmanager
from typing import Generator

@contextmanager
def execution_timer(label: str) -> Generator[None, None, None]:
    start = time.perf_counter()
    print(f"⏱️ Started [{label}]...")
    try:
        yield
    finally:
        elapsed = (time.perf_counter() - start) * 1000
        print(f"⏱️ Finished [{label}] in {elapsed:.2f} ms")


if __name__ == "__main__":
    with execution_timer("Matrix Operation"):
        total = sum(i**2 for i in range(500_000))
