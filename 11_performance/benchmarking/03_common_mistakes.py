"""
Common Mistakes in Code Benchmarking.
"""


# MISTAKE 1: Benchmarking code with `time.time()` instead of `time.perf_counter()`
def mistake_time_time() -> None:
    # DANGER: time.time() measures system wall-clock time and can be adjusted backwards by NTP clock sync!
    # ALWAYS use time.perf_counter() for high-precision, monotonic benchmarking!
    pass


if __name__ == "__main__":
    print("Always use time.perf_counter() or the timeit module for reliable, high-precision benchmarks!")
