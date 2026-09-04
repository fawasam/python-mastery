# `async` and `await` Keywords in Python

## What You Will Learn
* Concurrency via cooperative multitasking.
* Defining coroutines with `async def`.
* Yielding control to the event loop using `await`.
* `asyncio.run()` entry point.
* Synchronous vs Asynchronous execution model.

## Why This Matters
Traditional synchronous Python blocks the CPU thread whenever network I/O or file reads occur. `async` and `await` enable single-threaded cooperative concurrency, allowing your application to handle tens of thousands of concurrent I/O connections effortlessly.

## Prerequisites
* Functions (`01_beginner/13_functions`)
* Generators (`02_core_python/generators`)

## Core Concepts

### Coroutines and `await`
Functions defined with `async def` return a **coroutine object** when called. A coroutine does not execute immediately; it must be awaited or scheduled on an event loop.

```python
import asyncio

async def fetch_data(delay: float) -> str:
    print("Fetching data...")
    await asyncio.sleep(delay)  # Non-blocking pause
    return "Data retrieved"

async def main():
    result = await fetch_data(1.0)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
```

## Common Mistakes
* **Calling `async def` function without `await`**: Returns an un-awaited coroutine object instead of the return value!
* **Using `time.sleep()` inside `async def`**: `time.sleep()` is synchronous blocking and freezes the entire event loop. Use `await asyncio.sleep()`.

## Exercises
See `04_exercises.py` to practice defining and awaiting coroutines.
