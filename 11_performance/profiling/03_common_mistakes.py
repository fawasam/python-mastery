"""
Common Mistakes in Code Profiling.
"""


# MISTAKE 1: Profiling debug/test builds instead of production execution mode
def mistake_profiling_overhead() -> None:
    # DANGER: Profiling with active print statements or debug loggers inflates I/O metrics!
    # Always turn off verbose debugging logs when running performance profiling sessions!
    pass


if __name__ == "__main__":
    print("Always profile production-like workloads with debug logging disabled for accurate metrics!")
