"""
Advanced Architecture: Unit of Work & Transactional Boundaries.
"""

from typing import Protocol


class UnitOfWork(Protocol):
    """Abstraction for managing database transactions and committing atomic work."""
    def __enter__(self) -> "UnitOfWork":
        ...

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        ...

    def commit(self) -> None:
        ...

    def rollback(self) -> None:
        ...


class InMemoryUnitOfWork:
    def __enter__(self) -> "InMemoryUnitOfWork":
        print("[UoW] Started transaction context")
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        if exc_type is not None:
            self.rollback()
        else:
            self.commit()

    def commit(self) -> None:
        print("[UoW] Transaction committed successfully.")

    def rollback(self) -> None:
        print("[UoW] Transaction rolled back due to error.")


if __name__ == "__main__":
    uow = InMemoryUnitOfWork()
    
    with uow:
        print("Performing state updates within Unit of Work...")
