# Asyncio Tasks in Python

## What You Will Learn
* Scheduling background coroutines with `asyncio.create_task()`.
* Monitoring Task status (`task.done()`, `task.result()`, `task.cancel()`).
* Managing task lifecycles and background worker pools.
* Python 3.11+ `asyncio.TaskGroup` for structured concurrency.

## Why This Matters
While awaiting a coroutine executes it sequentially, `asyncio.create_task()` immediately wraps and schedules a coroutine on the event loop for background execution. This allows you to launch background background jobs while continuing main task processing.

## Prerequisites
* `async` & `await` (`09_async_python/async_await`)

## Core Concepts

### 1. `asyncio.create_task()`
```python
import asyncio

async def background_worker():
    await asyncio.sleep(1.0)
    print("Background work finished")

async def main():
    # Schedules task on event loop immediately
    task = asyncio.create_task(background_worker())
    print("Main continues while worker runs in background...")
    await task  # Wait for task completion when needed
```

### 2. Structured Concurrency (`asyncio.TaskGroup`)
```python
async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(job1())
        t2 = tg.create_task(job2())
    # Guarantees both t1 and t2 finish (or cancel cleanly on exception) before block exits!
```

## Exercises
See `04_exercises.py` to practice creating background tasks and task groups.
