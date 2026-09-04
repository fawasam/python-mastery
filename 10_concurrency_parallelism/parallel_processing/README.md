# Parallel Processing & Architectural Comparison in Python

## What You Will Learn
* Comparing Concurrency & Parallelism paradigms:
  - **Synchronous**: Single-threaded execution.
  - **Threading**: Single-process I/O concurrency (`threading`).
  - **Multiprocessing**: Multi-process CPU parallelism (`multiprocessing`).
  - **Asyncio**: Single-threaded cooperative I/O concurrency (`asyncio`).
* Choosing the right model for specific workloads.
* Chunking large datasets for multi-core parallel processing.

## Why This Matters
Selecting the correct execution model is critical for application performance. Running CPU-bound tasks in `threading` fails due to the GIL; running blocking disk I/O in `asyncio` freezes the event loop.

## Matrix Comparison Table
| Model | Process Count | Thread Count | Primary Use Case | GIL Bound? |
|---|---|---|---|---|
| Synchronous | 1 | 1 | Simple scripts, linear logic | Yes |
| Threading | 1 | N | I/O-bound (Sockets, DBs) | Yes |
| Multiprocessing | N | N | CPU-bound (Math, AI, ML) | No |
| Asyncio | 1 | 1 | High-concurrency I/O (Web APIs) | Yes |

## Exercises
See `04_exercises.py` to practice chunking data for process pool mapping.
