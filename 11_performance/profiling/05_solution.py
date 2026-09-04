"""
Solutions for Profiling Exercises.
"""

import cProfile
from typing import Callable


def count_function_calls(func: Callable) -> int:
    profiler = cProfile.Profile()
    profiler.enable()
    func()
    profiler.disable()
    return profiler.total_calls


def sample_target() -> None:
    _ = [x * 2 for x in range(1000)]


if __name__ == "__main__":
    calls = count_function_calls(sample_target)
    assert calls > 0
    print(f"Total profile call count: {calls}")
