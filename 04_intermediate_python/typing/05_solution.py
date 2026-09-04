"""
Topic: Typing Solutions
File: 05_solution.py
"""
from typing import Callable, Generic, Literal, TypeVar

HTTPMethod = Literal["GET", "POST", "PUT", "DELETE"]

T = TypeVar("T")
R = TypeVar("R")
K = TypeVar("K")
V = TypeVar("V")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        if not self._items:
            raise IndexError("Pop from empty stack")
        return self._items.pop()


def transform_elements(items: list[T], mapper: Callable[[T], R]) -> list[R]:
    return [mapper(item) for item in items]


class CacheContainer(Generic[K, V]):
    def __init__(self) -> None:
        self._store: dict[K, V] = {}

    def set(self, key: K, value: V) -> None:
        self._store[key] = value

    def get(self, key: K) -> V | None:
        return self._store.get(key)


if __name__ == "__main__":
    print("--- Level 2 ---")
    s = Stack[int]()
    s.push(10)
    s.push(20)
    print(f"Popped: {s.pop()}")

    print("\n--- Level 3 ---")
    nums = [1, 2, 3]
    doubled = transform_elements(nums, lambda x: x * 2)
    print(f"Doubled: {doubled}")

    print("\n--- Level 4 ---")
    cache = CacheContainer[str, int]()
    cache.set("user_count", 42)
    print(f"Cached user count: {cache.get('user_count')}")
