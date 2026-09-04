"""
Topic: Iterator Solutions
File: 05_solution.py
"""
from typing import Any

def level_1_easy() -> None:
    it = iter("PYTHON")
    while True:
        try:
            char = next(it)
            print(f"Char: {char}")
        except StopIteration:
            break


class EvenNumbers:
    def __init__(self, max_val: int) -> None:
        self.max_val = max_val
        self.current = 0

    def __iter__(self) -> "EvenNumbers":
        return self

    def __next__(self) -> int:
        if self.current > self.max_val:
            raise StopIteration
        val = self.current
        self.current += 2
        return val


def level_2_medium() -> list[int]:
    evens = list(EvenNumbers(10))
    print(f"Even numbers up to 10: {evens}")
    return evens


class BatchIterator:
    def __init__(self, data: list[Any], batch_size: int) -> None:
        self.data = data
        self.batch_size = batch_size
        self.index = 0

    def __iter__(self) -> "BatchIterator":
        return self

    def __next__(self) -> list[Any]:
        if self.index >= len(self.data):
            raise StopIteration
        batch = self.data[self.index : self.index + self.batch_size]
        self.index += self.batch_size
        return batch


def level_4_real_world() -> None:
    data = list(range(1, 10))
    batch_it = BatchIterator(data, batch_size=3)
    print("Batches of 3:")
    for batch in batch_it:
        print(f"  Batch: {batch}")


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium()

    print("\n--- Level 4 ---")
    level_4_real_world()
