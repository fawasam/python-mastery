"""
Common Mistakes with Python Garbage Collection.
"""

import gc
import time


# MISTAKE: Explicitly calling gc.collect() inside tight loops
def bad_gc_in_loop() -> None:
    print("--- Executing BAD pattern: gc.collect() inside tight loop ---")
    start = time.perf_counter()
    for _ in range(500):
        data = [x for x in range(100)]
        gc.collect()  # HUGE PERFORMANCE PENALTY! Runs full traversal scan on every iteration
    duration = time.perf_counter() - start
    print(f"Time taken with bad gc in loop: {duration:.4f} seconds")


# GOOD: Let automatic GC run according to generation thresholds
def good_gc_usage() -> None:
    print("\n--- Executing GOOD pattern: Standard automatic GC ---")
    start = time.perf_counter()
    for _ in range(500):
        data = [x for x in range(100)]
    duration = time.perf_counter() - start
    print(f"Time taken with standard GC: {duration:.4f} seconds")


if __name__ == "__main__":
    bad_gc_in_loop()
    good_gc_usage()
