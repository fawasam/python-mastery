"""
Benchmarking Sync vs Threading vs Multiprocessing for CPU-Bound Math.
"""

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time


def cpu_intensive_work(n: int = 5_000_000) -> int:
    return sum(i * i for i in range(n))


def main() -> None:
    inputs = [5_000_000] * 4

    # 1. ThreadPoolExecutor (Bound by GIL for CPU tasks)
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=4) as executor:
        _ = list(executor.map(cpu_intensive_work, inputs))
    t_threads = time.perf_counter() - t0

    # 2. ProcessPoolExecutor (Bypasses GIL across multi-core CPU processes)
    t1 = time.perf_counter()
    with ProcessPoolExecutor(max_workers=4) as executor:
        _ = list(executor.map(cpu_intensive_work, inputs))
    t_processes = time.perf_counter() - t1

    print(f"CPU Math with ThreadPoolExecutor (GIL Contention): {t_threads:.4f}s")
    print(f"CPU Math with ProcessPoolExecutor (True Parallel) : {t_processes:.4f}s")


if __name__ == "__main__":
    main()
