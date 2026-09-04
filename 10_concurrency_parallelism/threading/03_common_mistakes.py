"""
Common Mistakes in Python Threading.
"""


# MISTAKE 1: Expecting CPU speedups from threading due to the GIL
def mistake_cpu_bound_threading() -> None:
    # DANGER: Running heavy math / matrix calculations in multiple threading.Thread instances
    # causes thread context-switch overhead while GIL locks execution to a SINGLE core!
    # Use multiprocessing.Process or ProcessPoolExecutor for true multi-core CPU parallelism!
    pass


if __name__ == "__main__":
    print("Use threading for I/O-bound tasks (network, disk, DB), and multiprocessing for CPU-bound computation!")
