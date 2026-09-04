"""
Concurrent Futures Exercises.
"""

from concurrent.futures import ThreadPoolExecutor


def double_val(x: int) -> int:
    return x * 2


# Exercise 1 (Medium): Double values in ThreadPoolExecutor
# Write double_all_futures(values: list[int]) -> list[int]
# Uses ThreadPoolExecutor(max_workers=2) with executor.map to double all items.
def double_all_futures(values: list[int]) -> list[int]:
    raise NotImplementedError("Implement double_all_futures")
