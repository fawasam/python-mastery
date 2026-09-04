"""
Common Mistakes in Code Optimization.
"""


# MISTAKE 1: Optimizing without measuring first
def mistake_unmeasured_optimization() -> None:
    # DANGER: Rewriting clean, readable Python into unreadable micro-optimized tricks
    # BEFORE profiling where the actual bottleneck is located!
    pass


if __name__ == "__main__":
    print("Measure first with cProfile or timeit before altering code structure!")
