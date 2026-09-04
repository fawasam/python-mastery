"""
Practical GC Usage: Context Manager for Temporary GC Disabling in High-Performance Batches.
"""

from contextlib import contextmanager
import gc
import time


@contextmanager
def suppress_gc():
    """
    Context manager that temporarily disables GC during critical performance blocks
    and forces a collection when exiting.
    """
    was_enabled = gc.isenabled()
    if was_enabled:
        gc.disable()
    try:
        yield
    finally:
        if was_enabled:
            gc.enable()
            collected = gc.collect()
            print(f"[GC] Re-enabled and collected {collected} unreachable objects.")


def run_heavy_batch() -> None:
    print("Executing batch operation with GC suppressed...")
    dummy_data = []
    for i in range(100_000):
        dummy_data.append({"id": i, "data": [i]})


if __name__ == "__main__":
    start = time.perf_counter()
    with suppress_gc():
        run_heavy_batch()
    duration = time.perf_counter() - start
    print(f"Batch completed in {duration:.4f} seconds.")
