# Profiling Python Code (`cProfile`)

## What You Will Learn
* Python's standard profiling module `cProfile` and `pstats`.
* Identifying execution bottlenecks (function call counts `ncalls`, total time `tottime`, cumulative time `cumtime`).
* Sorting and filtering profile statistics.
* Programmatic profiling vs command-line profiling (`python -m cProfile script.py`).

## Why This Matters
"Premature optimization is the root of all evil" (Donald Knuth). Profiling replaces intuition with exact empirical measurement, showing you precisely which functions account for 80%+ of execution time before you spend time optimizing.

## Prerequisites
* Functions & Modules (`01_beginner/13_functions`, `01_beginner/15_modules`)

## Core Concepts

### Programmatic Profiling with `cProfile.Profile()`
```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# Code block to profile
run_heavy_function()

profiler.disable()
stats = pstats.Stats(profiler).sort_stats("cumtime")
stats.print_stats(10)  # Print top 10 bottleneck functions
```

## Exercises
See `04_exercises.py` to practice extracting top cumulative time functions with `cProfile`.
