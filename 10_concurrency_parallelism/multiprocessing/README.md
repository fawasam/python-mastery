# Multiprocessing & Multi-Core CPU Parallelism in Python

## What You Will Learn
* True multi-core CPU parallelism with Python's `multiprocessing` module (`multiprocessing.Process`).
* Bypassing the Global Interpreter Lock (GIL) via separate CPython process instances.
* Process pools (`multiprocessing.Pool` with `map` and `apply_async`).
* Inter-Process Communication (IPC) via `multiprocessing.Queue` and `Pipe`.

## Why This Matters
While threads share a single process space and are limited by the GIL, `multiprocessing` spawns distinct CPython process instances across separate CPU cores, providing true parallel CPU execution for heavy math, data processing, and machine learning workloads.

## Prerequisites
* Threading (`10_concurrency_parallelism/threading`)

## Core Concepts

### Process Pool Mapping
```python
import multiprocessing

def cpu_heavy_square(n: int) -> int:
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool() as pool:
        results = pool.map(cpu_heavy_square, [1, 2, 3, 4, 5])
        print(results)  # [1, 4, 9, 16, 25]
```

## Common Mistakes
* **Forgetting `if __name__ == "__main__":` guard**: On Windows and macOS (spawn start method), launching processes outside the main guard causes infinite recursive process spawning crashes!

## Exercises
See `04_exercises.py` to practice multi-core pool mapping.
