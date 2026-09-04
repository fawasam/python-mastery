"""
Basic Multiprocessing Pool Parallelism.
"""

import multiprocessing
import time


def compute_factorial(n: int) -> int:
    """CPU-heavy task executed across separate OS processes."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main() -> None:
    start = time.perf_counter()
    numbers = [5000 + i for i in range(8)]

    # Use multiprocessing.Pool to distribute computation across available CPU cores
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers)

    duration = time.perf_counter() - start
    print(f"Computed {len(results)} factorials across multi-core process pool in {duration:.4f}s")


if __name__ == "__main__":
    # MANDATORY: if __name__ == '__main__': protects process spawn entrypoint!
    main()
