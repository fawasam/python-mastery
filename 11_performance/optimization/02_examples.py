"""
Local Variable Caching inside Tight Loops.
"""

import time


# Global function lookup inside loop
def append_global_lookup(items: list[int]) -> list[str]:
    result = []
    # Every iteration performs global lookup for 'str' and method lookup for 'result.append'
    for item in items:
        result.append(str(item))
    return result


# Cached local function lookup inside loop
def append_local_cached(items: list[int]) -> list[str]:
    result = []
    # Local variable lookups execute via C-array LOAD_FAST offsets!
    append_func = result.append
    str_func = str
    for item in items:
        append_func(str_func(item))
    return result


def main() -> None:
    data = list(range(500_000))

    t0 = time.perf_counter()
    _ = append_global_lookup(data)
    t_global = time.perf_counter() - t0

    t1 = time.perf_counter()
    _ = append_local_cached(data)
    t_local = time.perf_counter() - t1

    print(f"Global Lookup Time: {t_global * 1000:.2f} ms")
    print(f"Local Cached Time : {t_local * 1000:.2f} ms")


if __name__ == "__main__":
    main()
