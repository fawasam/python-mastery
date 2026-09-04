# Coroutines & Generator-Based Coroutines in Python

## What You Will Learn
* History of Coroutines in Python (Generator-based `yield` vs Native `async def`).
* Coroutine state transitions (`GEN_CREATED`, `GEN_RUNNING`, `GEN_SUSPENDED`, `GEN_CLOSED`).
* Inspecting coroutine states via `inspect.getcoroutinestate()`.
* Sending values into generator-based coroutines with `.send()`.

## Why This Matters
Understanding native coroutine objects and their internal suspension state mechanisms solidifies your mental model of how the CPython event loop context-switches between concurrent tasks.

## Prerequisites
* `async` & `await` (`09_async_python/async_await`)
* Generators (`02_core_python/generators`)

## Core Concepts

### Coroutine Inspection
```python
import inspect

async def my_coro():
    await asyncio.sleep(1)

c = my_coro()
print(inspect.getcoroutinestate(c))  # CORO_CREATED
```

## Exercises
See `04_exercises.py` to practice inspecting coroutine states.
