# Algorithmic & Code Optimization in Python

## What You Will Learn
* Optimizing Python code performance systematically.
* Algorithmic complexity reduction (O(N^2) -> O(N log N) -> O(N) -> O(1)).
* Replacing explicit Python loops with C-optimized builtins (`sum()`, `any()`, `all()`, `map()`).
* String concatenation optimization (`str.join()`).
* Local variable caching inside tight loops.

## Why This Matters
Writing Pythonic, performant code is not about micro-optimization tricks; it is about choosing optimal data structures and delegating loop iterations to CPython built-in C-extensions whenever possible.

## Prerequisites
* Profiling & Benchmarking (`11_performance/profiling`, `11_performance/benchmarking`)

## Core Concepts

### String Concatenation Optimization
Bad (O(N^2) memory reallocation):
```python
s = ""
for item in str_list:
    s += item
```

Good (O(N) single buffer allocation):
```python
s = "".join(str_list)
```

## Exercises
See `04_exercises.py` to practice refactoring nested loops into set intersections.
