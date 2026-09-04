# The Asyncio Event Loop in Python

## What You Will Learn
* The CPython Event Loop mechanism (`asyncio.get_running_loop()`).
* Scheduling callbacks (`loop.call_soon()`, `loop.call_later()`).
* Running CPU-bound tasks in thread/process pools via `loop.run_in_executor()`.
* Understanding selector-based I/O multiplexing (`select` / `epoll` / `kqueue`).

## Why This Matters
The event loop is the engine driving all `asyncio` code. Knowing how to interface with the running loop and offload heavy CPU-bound computations (like image processing or cryptography) to `run_in_executor` keeps the event loop responsive.

## Prerequisites
* Async Tasks (`09_async_python/tasks`)

## Core Concepts

### Running CPU-Bound Code without Blocking the Event Loop
```python
import asyncio
import time

def heavy_cpu_computation(n: int) -> int:
    time.sleep(1.0)  # Heavy CPU calculation
    return n * n

async def main():
    loop = asyncio.get_running_loop()
    # Offload CPU bound call to default ThreadPoolExecutor
    result = await loop.run_in_executor(None, heavy_cpu_computation, 10)
    print(result)
```

## Exercises
See `04_exercises.py` to practice offloading synchronous functions via `run_in_executor`.
