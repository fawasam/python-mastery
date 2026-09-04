"""
Statistical Benchmarking using timeit.repeat().
"""

import timeit


def demo_timeit_repeat() -> None:
    # Measure execution time 5 times with 10,000 iterations per run
    times = timeit.repeat("'-'.join(str(n) for n in range(100))", number=10_000, repeat=5)

    best_time = min(times)
    avg_time = sum(times) / len(times)

    print(f"Timeit Repeat Results (5 runs x 10,000 iterations):")
    print(f" Best Time: {best_time:.4f}s")
    print(f" Avg Time : {avg_time:.4f}s")


if __name__ == "__main__":
    demo_timeit_repeat()
