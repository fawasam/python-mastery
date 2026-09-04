"""
Solutions for Descriptor Exercises.
"""


class NonEmptyString:
    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    def __get__(self, instance: object | None, owner: type | None = None) -> object:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, "")

    def __set__(self, instance: object, value: object) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Value must be a non-empty string.")
        setattr(instance, self.storage_name, value.strip())


class TypedField:
    def __init__(self, expected_type: type) -> None:
        self.expected_type = expected_type

    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    def __get__(self, instance: object | None, owner: type | None = None) -> object:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)

    def __set__(self, instance: object, value: object) -> None:
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected type {self.expected_type.__name__}, got {type(value).__name__}")
        setattr(instance, self.storage_name, value)


class Product:
    name = NonEmptyString()
    stock = TypedField(int)

    def __init__(self, name: str, stock: int) -> None:
        self.name = name
        self.stock = stock


if __name__ == "__main__":
    p = Product("Gadget", 100)
    print(f"Product: {p.name}, Stock: {p.stock}")

    try:
        p.name = "   "
    except ValueError as e:
        print(f"Validation Caught: {e}")

    try:
        p.stock = "out of stock"
    except TypeError as e:
        print(f"Type Check Caught: {e}")
