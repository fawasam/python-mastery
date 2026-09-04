# Benchmarking Code Performance (`timeit` / `perf_counter`)

## What You Will Learn
* Python's standard `timeit` module.
* High-precision timing using `time.perf_counter()`.
* Comparing execution times of competing algorithms or data structures.
* Statistical measurement across multiple repetitions (`timeit.repeat()`).

## Why This Matters
Benchmarking measures how fast alternative implementations run under standardized conditions. It answers questions like: "Is a set lookup faster than a list lookup?", "Is a list comprehension faster than `map()`?", or "Does vectorization improve performance by 10x?".

## Prerequisites
* Profiling (`11_performance/profiling`)

## Core Concepts

### Benchmarking with `timeit.timeit()`
```python
import timeit

# Benchmark list comprehension vs map
t_comp = timeit.timeit("[x * 2 for x in range(1000)]", number=10000)
t_map = timeit.timeit("list(map(lambda x: x * 2, range(1000)))", number=10000)

print(f"Comprehension: {t_comp:.4f}s | Map: {t_map:.4f}s")
```

## Exercises
See `04_exercises.py` to practice benchmarking list vs set membership lookup speed.
