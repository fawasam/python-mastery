# Solution Explanation: Hybrid Concurrency & Parallelism Processing Pipeline

## Architectural Decisions

1. **`ThreadPoolExecutor` for I/O Phase**:
   I/O network operations release the Python GIL while waiting for socket bytes. Threading is lightweight and allows multiple threads to wait concurrently within a single process.

2. **`ProcessPoolExecutor` for CPU Phase**:
   Heavy hashing and data parsing are CPU-intensive. ProcessPoolExecutor spawns distinct OS process instances across physical CPU cores, bypassing GIL lock contention completely.
