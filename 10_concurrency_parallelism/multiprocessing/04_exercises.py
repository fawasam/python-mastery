"""
Multiprocessing Exercises.
"""

import multiprocessing


def compute_cube(n: int) -> int:
    return n**3


# Exercise 1 (Medium): Parallel Cubes with Pool
# Write parallel_cubes(numbers: list[int]) -> list[int]
# Uses multiprocessing.Pool() to map compute_cube over numbers.
def parallel_cubes(numbers: list[int]) -> list[int]:
    raise NotImplementedError("Implement parallel_cubes using multiprocessing.Pool")
