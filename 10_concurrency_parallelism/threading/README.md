# Threading & GIL in Python

## What You Will Learn
* Multithreading using Python's `threading` module (`threading.Thread`).
* Global Interpreter Lock (GIL) and its impact on CPU-bound vs I/O-bound tasks.
* Starting, joining, and daemon threads (`t.start()`, `t.join()`, `daemon=True`).
* Sharing memory across threads in a single process space.

## Why This Matters
Python threads run within a single process. Because of the Global Interpreter Lock (GIL), only one OS thread executes Python bytecode at a time. Threading is ideal for **I/O-bound operations** (file I/O, network requests, database waits), allowing other threads to run while one thread waits for I/O.

## Prerequisites
* Functions & Scope (`01_beginner/13_functions`, `01_beginner/14_scope`)

## Core Concepts

### Thread Creation
```python
import threading
import time

def worker_task(name: str):
    print(f"Worker {name} started")
    time.sleep(1.0)  # Releases GIL during sleep!
    print(f"Worker {name} finished")

t1 = threading.Thread(target=worker_task, args=("Thread-1",))
t2 = threading.Thread(target=worker_task, args=("Thread-2",))

t1.start()
t2.start()

t1.join()  # Wait for t1 to complete
t2.join()  # Wait for t2 to complete
```

## Common Mistakes
* **Using `threading` for CPU-bound computation**: Due to GIL contention, running CPU-heavy calculations in multiple Python threads runs SLOWER than a single thread! Use `multiprocessing` for CPU-bound parallelism.

## Exercises
See `04_exercises.py` to practice creating thread pools and worker threads.
