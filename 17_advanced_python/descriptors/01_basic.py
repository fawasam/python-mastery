"""
Descriptors Basics: Validated Numeric Attribute Descriptor.
"""

from typing import Any


class BoundedInteger:
    """Descriptor enforcing integer range constraints (min_val <= val <= max_val)."""
    def __init__(self, min_val: int, max_val: int) -> None:
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    def __get__(self, instance: Any, owner: type) -> Any:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, self.min_val)

    def __set__(self, instance: Any, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        if not (self.min_val <= value <= self.max_val):
            raise ValueError(f"Value {value} out of range [{self.min_val}, {self.max_val}]")
        setattr(instance, self.storage_name, value)


class UserProfile:
    age = BoundedInteger(min_val=18, max_val=120)

    def __init__(self, age: int) -> None:
        self.age = age


if __name__ == "__main__":
    user = UserProfile(age=25)
    print(f"Validated user age: {user.age}")
