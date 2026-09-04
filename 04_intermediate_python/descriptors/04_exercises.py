"""
Descriptor Exercises.

Implement descriptors to validate types and log changes.
"""


# Exercise 1 (Easy): NonEmptyString Descriptor
# Create a descriptor NonEmptyString that raises ValueError if set to a non-string or empty/whitespace string.
class NonEmptyString:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    def __get__(self, instance: object | None, owner: type | None = None) -> object:
        raise NotImplementedError("Implement __get__")

    def __set__(self, instance: object, value: object) -> None:
        raise NotImplementedError("Implement __set__")


# Exercise 2 (Medium): TypedField Descriptor
# Create a descriptor TypedField(expected_type) that ensures assigned values match expected_type.
class TypedField:
    def __init__(self, expected_type: type) -> None:
        self.expected_type = expected_type

    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    def __get__(self, instance: object | None, owner: type | None = None) -> object:
        raise NotImplementedError("Implement __get__")

    def __set__(self, instance: object, value: object) -> None:
        raise NotImplementedError("Implement __set__")
