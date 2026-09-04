"""
Topic: Singleton Pattern via __new__
File: 02_examples.py
"""
from typing import Any, Self

class SingletonDatabaseConnection:
    _instance: Self | None = None

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        if cls._instance is None:
            print("  [__new__] Creating unique Singleton instance...")
            cls._instance = super().__new__(cls)
        return cls._instance


if __name__ == "__main__":
    db1 = SingletonDatabaseConnection()
    db2 = SingletonDatabaseConnection()

    print(f"db1 id: {id(db1)}")
    print(f"db2 id: {id(db2)}")
    print(f"Are db1 and db2 the exact same instance? {db1 is db2}")
