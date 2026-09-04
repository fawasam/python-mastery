# Locks & Synchronization Primitives in Python

## What You Will Learn
* Race conditions and critical sections.
* Mutual exclusion using `threading.Lock()` (`lock.acquire()`, `lock.release()`, `with lock:`).
* Reentrant locks (`threading.RLock()`).
* Semaphores (`threading.Semaphore()`).
* Preventing deadlocks.

## Why This Matters
When multiple threads read and write shared memory simultaneously without synchronization, **race conditions** occur, leading to data corruption and non-deterministic bugs. Locks enforce exclusive access to critical sections of code.

## Prerequisites
* Threading (`10_concurrency_parallelism/threading`)

## Core Concepts

### Thread Synchronization with Context Manager (`with lock:`)
```python
import threading

shared_counter = 0
lock = threading.Lock()

def safe_increment():
    global shared_counter
    # 'with lock:' acquires the lock before entering and auto-releases it on exit
    with lock:
        shared_counter += 1
```

### RLock (Reentrant Lock)
`RLock` allows the SAME thread to acquire the lock multiple times without deadlocking itself (useful for recursive function calls or nested method invocations within the same class).

## Exercises
See `04_exercises.py` to practice fixing race conditions with `threading.Lock()`.
