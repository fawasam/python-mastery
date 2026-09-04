# Mini Project: Parallel Task & Processing Engine

## Overview
This mini project combines multithreading and multi-process parallelism into a hybrid processing pipeline:
1. **I/O Phase (`ThreadPoolExecutor`)**: Concurrently fetches raw payloads from network endpoints without blocking main execution.
2. **CPU Phase (`ProcessPoolExecutor`)**: Distributes CPU-heavy data parsing and mathematical hashing across multi-core OS processes, bypassing the GIL.

## How to Run
```bash
python main.py
```
