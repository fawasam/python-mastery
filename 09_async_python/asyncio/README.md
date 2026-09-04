# `asyncio` Standard Library Module in Python

## What You Will Learn
* The Python standard library `asyncio` ecosystem.
* `asyncio.run()`, `asyncio.gather()`, `asyncio.sleep()`.
* Timeouts with `asyncio.timeout()` (Python 3.11+) and `asyncio.wait_for()`.
* Handling cancellation with `asyncio.CancelledError`.

## Why This Matters
`asyncio` provides asynchronous I/O framework primitives for network services, web crawlers, databases, and message queues.

## Prerequisites
* `async` & `await` (`09_async_python/async_await`)

## Core Concepts

### Timeouts with `asyncio.wait_for`
```python
import asyncio

async def slow_task():
    await asyncio.sleep(10.0)

async def main():
    try:
        await asyncio.wait_for(slow_task(), timeout=1.0)
    except TimeoutError:
        print("Task timed out after 1.0s!")
```

## Exercises
See `04_exercises.py` to practice handling timeouts and cancellations.
