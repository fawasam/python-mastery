"""
Solutions: Descriptors Exercises.
"""

from typing import Any


class StringTypeDescriptor:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    def __get__(self, instance: Any, owner: type) -> Any:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, "")

    def __set__(self, instance: Any, value: Any) -> None:
        if not isinstance(value, str):
            raise TypeError("Attribute must be a string")
        setattr(instance, self.storage_name, value)


class Person:
    name = StringTypeDescriptor()


if __name__ == "__main__":
    p = Person()
    p.name = "Alice"
    print("Person name:", p.name)
