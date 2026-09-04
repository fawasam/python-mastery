"""
Context Managers Basics: Re-entrant ExitStack and contextmanager decorator.
"""

from contextlib import contextmanager
import time
from typing import Generator


@contextmanager
def execution_timer(task_name: str) -> Generator[None, None, None]:
    """Generator-based context manager measuring code block execution time."""
    start = time.perf_counter()
    try:
        print(f"[{task_name}] Started task...")
        yield
    finally:
        duration = time.perf_counter() - start
        print(f"[{task_name}] Completed in {duration:.4f} seconds.")


if __name__ == "__main__":
    with execution_timer("Database Query"):
        time.sleep(0.01)
