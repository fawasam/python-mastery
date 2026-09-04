"""
Solutions: Generators Exercises.
"""

from typing import Generator


def infinite_counter(start: int = 0) -> Generator[int, None, None]:
    curr = start
    while True:
        yield curr
        curr += 1


if __name__ == "__main__":
    gen = infinite_counter(10)
    first_three = [next(gen), next(gen), next(gen)]
    print("First three generated values:", first_three)
