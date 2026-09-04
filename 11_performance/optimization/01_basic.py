"""
Basic Loop Optimization: Replacing Explicit Loops with C-Builtins.
"""

import time


# Slow O(N) explicit Python loop
def sum_explicit_loop(numbers: list[int]) -> int:
    total = 0
    for n in numbers:
        total += n
    return total


# Fast O(N) C-Optimized Builtin sum()
def sum_c_builtin(numbers: list[int]) -> int:
    return sum(numbers)


def main() -> None:
    nums = list(range(1_000_000))

    t0 = time.perf_counter()
    res1 = sum_explicit_loop(nums)
    t_explicit = time.perf_counter() - t0

    t1 = time.perf_counter()
    res2 = sum_c_builtin(nums)
    t_builtin = time.perf_counter() - t1

    assert res1 == res2
    print(f"Explicit Python Loop: {t_explicit * 1000:.2f} ms")
    print(f"C-Optimized Builtin  : {t_builtin * 1000:.2f} ms")
    print(f"Builtin Speedup      : {t_explicit / t_builtin:.1f}x faster!")


if __name__ == "__main__":
    main()
