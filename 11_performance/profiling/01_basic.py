"""
Basic Profiling using cProfile and pstats.
"""

import cProfile
import io
import pstats


def slow_computation() -> int:
    total = 0
    for i in range(500_000):
        total += i * i
    return total


def fast_computation() -> int:
    return sum(range(100))


def main_workflow() -> None:
    _ = slow_computation()
    _ = fast_computation()


def run_profiler() -> None:
    profiler = cProfile.Profile()
    profiler.enable()

    main_workflow()

    profiler.disable()

    # Capture formatted statistics output
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream).sort_stats(pstats.SortKey.CUMULATIVE)
    stats.print_stats(5)

    print("--- Top Bottleneck Functions (Sorted by Cumulative Time) ---")
    print(stream.getvalue())


if __name__ == "__main__":
    run_profiler()
