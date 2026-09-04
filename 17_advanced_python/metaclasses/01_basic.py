"""
Metaclasses Basics: Enforcing Snake Case Method Names.
"""

from typing import Any


class SnakeCaseMeta(type):
    """Metaclass that validates all attribute names of a class use lowercase snake_case."""
    def __new__(cls, name: str, bases: tuple[type, ...], dct: dict[str, Any]) -> Any:
        for attr_name in dct:
            if not attr_name.startswith("__") and any(c.isupper() for c in attr_name):
                raise TypeError(f"Method/attribute '{attr_name}' in class '{name}' must be lowercase_snake_case!")
        return super().__new__(cls, name, bases, dct)


class ValidClass(metaclass=SnakeCaseMeta):
    def valid_method_name(self) -> str:
        return "OK"


if __name__ == "__main__":
    obj = ValidClass()
    print("Class created successfully with valid method:", obj.valid_method_name())
