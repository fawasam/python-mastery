"""
Solutions for Benchmarking Exercises.
"""

import time
from typing import Callable


def measure_execution_ms(func: Callable) -> float:
    t0 = time.perf_counter()
    func()
    return (time.perf_counter() - t0) * 1000.0


def sample_work() -> None:
    time.sleep(0.01)


if __name__ == "__main__":
    duration_ms = measure_execution_ms(sample_work)
    assert duration_ms >= 10.0
    print(f"Measured function duration: {duration_ms:.2f} ms")
