"""
Solutions for Concurrent Futures Exercises.
"""

from concurrent.futures import ThreadPoolExecutor


def double_val(x: int) -> int:
    return x * 2


def double_all_futures(values: list[int]) -> list[int]:
    with ThreadPoolExecutor(max_workers=2) as executor:
        return list(executor.map(double_val, values))


if __name__ == "__main__":
    results = double_all_futures([1, 2, 3, 4])
    assert results == [2, 4, 6, 8]
    print(f"Double all futures exercise passed successfully! Results: {results}")
