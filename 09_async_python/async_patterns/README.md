# Async Design Patterns in Python

## What You Will Learn
* Producer-Consumer Pattern using `asyncio.Queue`.
* Asynchronous Generators (`async def` with `yield`).
* Asynchronous Iterators (`__aiter__` and `__anext__`).
* Event Signaling (`asyncio.Event`).

## Why This Matters
Building scalable asynchronous architectures requires messaging queues, event-driven task dispatching, and streaming data pipelines. `asyncio.Queue` and async generators provide high-throughput pipeline components.

## Prerequisites
* Async Tasks (`09_async_python/tasks`)
* Generators & Iterators (`02_core_python/generators`, `02_core_python/iterators`)

## Core Concepts

### 1. `asyncio.Queue` Producer-Consumer Pattern
```python
import asyncio

async def producer(queue: asyncio.Queue):
    for i in range(5):
        await queue.put(f"item_{i}")
        await asyncio.sleep(0.01)

async def consumer(queue: asyncio.Queue):
    while True:
        item = await queue.get()
        print(f"Consumed {item}")
        queue.task_done()
```

### 2. Async Generator (`async def` + `yield`)
```python
async def async_range(count: int):
    for i in range(count):
        await asyncio.sleep(0.01)
        yield i

async def main():
    async for num in async_range(3):
        print(num)
```

## Exercises
See `04_exercises.py` to practice building `asyncio.Queue` worker pipelines.
