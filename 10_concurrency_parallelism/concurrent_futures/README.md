# Modern High-Level Execution via `concurrent.futures`

## What You Will Learn
* Python's high-level `concurrent.futures` module interface.
* `ThreadPoolExecutor` for I/O-bound task pools.
* `ProcessPoolExecutor` for CPU-bound task pools.
* `Future` objects (`future.result()`, `future.done()`).
* Batch mapping with `executor.map()` and `as_completed()`.

## Why This Matters
`concurrent.futures` provides a unified, high-level API over both thread pools and process pools. Switching between thread-based concurrency and multi-process parallelism requires changing only a single class name (`ThreadPoolExecutor` vs `ProcessPoolExecutor`).

## Prerequisites
* Threading & Multiprocessing (`10_concurrency_parallelism/threading`, `10_concurrency_parallelism/multiprocessing`)

## Core Concepts

### Unified Executor Pattern
```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed

def task(n: int) -> int:
    return n * 2

# ThreadPoolExecutor for I/O tasks
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(task, i) for i in range(5)]
    for f in as_completed(futures):
        print(f.result())
```

## Exercises
See `04_exercises.py` to practice submitting tasks to `ThreadPoolExecutor`.
