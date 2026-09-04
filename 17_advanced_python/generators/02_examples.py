"""
Advanced Generators: Delegating Sub-Generators using yield from.
"""

from typing import Generator


def sub_sequence(start: int, count: int) -> Generator[int, None, None]:
    for i in range(start, start + count):
        yield i


def master_sequence() -> Generator[int, None, None]:
    """Master generator delegating sequence generation using yield from."""
    yield 0
    yield from sub_sequence(10, 3)  # Yields 10, 11, 12 transparently
    yield from sub_sequence(100, 2) # Yields 100, 101 transparently
    yield 999


if __name__ == "__main__":
    result = list(master_sequence())
    print("Delegated Sequence Output:", result)
