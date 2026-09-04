"""
Basic Benchmarking: Set vs List Membership Lookup Speed.
"""

import time


def benchmark_membership_lookup() -> None:
    size = 100_000
    search_target = 99_999

    dataset_list = list(range(size))
    dataset_set = set(range(size))

    # Benchmark List Lookup O(N)
    t0 = time.perf_counter()
    _ = search_target in dataset_list
    t_list = time.perf_counter() - t0

    # Benchmark Set Lookup O(1)
    t1 = time.perf_counter()
    _ = search_target in dataset_set
    t_set = time.perf_counter() - t1

    print(f"List Lookup O(N) Time: {t_list * 1000:.6f} ms")
    print(f"Set Lookup  O(1) Time: {t_set * 1000:.6f} ms")
    speedup = t_list / t_set if t_set > 0 else 1.0
    print(f"Set Lookup Speedup: {speedup:.1f}x faster!")


if __name__ == "__main__":
    benchmark_membership_lookup()
