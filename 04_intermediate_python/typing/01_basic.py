"""
Topic: Generics & Literal Types
File: 01_basic.py
"""
from typing import Generic, Literal, TypeVar

T = TypeVar("T")

class Repository(Generic[T]):
    def __init__(self) -> None:
        self._storage: dict[int, T] = {}

    def save(self, entity_id: int, entity: T) -> None:
        self._storage[entity_id] = entity

    def get(self, entity_id: int) -> T | None:
        return self._storage.get(entity_id)


AccessMode = Literal["READ_ONLY", "READ_WRITE", "ADMIN"]

def configure_access(mode: AccessMode) -> None:
    print(f"Configured access mode: {mode}")


if __name__ == "__main__":
    string_repo = Repository[str]()
    string_repo.save(1, "User Data Record")
    print(f"Retrieved: {string_repo.get(1)}")

    configure_access("READ_ONLY")
