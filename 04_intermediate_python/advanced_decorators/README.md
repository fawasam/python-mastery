# Advanced Decorators in Python

## What You Will Learn
* Decorators that accept arguments (`@repeat(num_times=3)`).
* Class-based decorators implementing `__call__`.
* Decorating classes directly (class decorators).
* Preserving signature & metadata with `@functools.wraps`.
* Decorator chaining and execution order.

## Why This Matters
Decorators are pervasive in Python frameworks (FastAPI routes `@app.get`, Flask `@app.route`, Pytest `@pytest.mark`, Click CLI decorators). Advanced decorators let you dynamically modify behavior, perform validation, enforce authorization, and add metrics without altering core logic.

## Prerequisites
* Core Decorators (`02_core_python/decorators`)
* Closures (`04_intermediate_python/closures`)

## Core Concepts

### Decorators with Arguments (3-tier nested functions)
To pass arguments to a decorator, you create a function that takes the arguments and returns the actual decorator function:

```python
import functools

def repeat(num_times: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator
```

### Class-Based Decorators
```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        return self.func(*args, **kwargs)
```

## Common Mistakes
* **Forgetting `@functools.wraps`**: Strips `__name__`, `__doc__`, and function signatures, breaking introspection and documentation tools.
* **Confusing execution order when chaining decorators**: `@decorator_a` over `@decorator_b` executes `A(B(func))`.

## Exercises
See `04_exercises.py` to practice building parametrized retry decorators and timer class decorators.
