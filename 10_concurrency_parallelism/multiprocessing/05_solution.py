"""
Solutions for Multiprocessing Exercises.
"""

import multiprocessing


def compute_cube(n: int) -> int:
    return n**3


def parallel_cubes(numbers: list[int]) -> list[int]:
    with multiprocessing.Pool() as pool:
        return pool.map(compute_cube, numbers)


if __name__ == "__main__":
    cubes = parallel_cubes([1, 2, 3, 4])
    assert cubes == [1, 8, 27, 64]
    print(f"Parallel cubes exercise passed successfully! Results: {cubes}")
