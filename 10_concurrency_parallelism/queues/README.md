# Thread-Safe Queues (`queue.Queue`) in Python

## What You Will Learn
* Thread-safe Queue communication with Python's standard `queue` module.
* `FIFO Queue` (`queue.Queue`), `LIFO Queue` (`queue.LifoQueue`), and `PriorityQueue` (`queue.PriorityQueue`).
* Thread synchronization using `q.put()`, `q.get()`, `q.task_done()`, and `q.join()`.
* Producer-Consumer thread pool architecture.

## Why This Matters
When multiple OS threads run concurrently in Python, sharing raw global data structures like `list` or `dict` causes race conditions and memory corruption. `queue.Queue` provides built-in thread safety with internal locks and condition variables.

## Prerequisites
* Threading (`10_concurrency_parallelism/threading`)

## Core Concepts

### Thread-Safe Queue Pattern
```python
import queue
import threading

task_queue = queue.Queue(maxsize=10)

def worker():
    while True:
        item = task_queue.get()
        if item is None:  # Sentinel value to terminate thread
            break
        print(f"Processing {item}")
        task_queue.task_done()
```

## Exercises
See `04_exercises.py` to practice building thread-safe queue pipelines.
