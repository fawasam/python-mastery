"""
Advanced Descriptor Examples: Validation and Lazy Property Caching.
"""

from typing import Any, Callable, TypeVar

T = TypeVar("T")


class BoundedNumber:
    """
    Data descriptor enforcing minimum and maximum numeric bounds.
    """

    def __init__(self, min_val: float | None = None, max_val: float | None = None) -> None:
        self.min_val = min_val
        self.max_val = max_val

    def __set_name__(self, owner: type, name: str) -> None:
        self.storage_name = f"_{name}"

    def __get__(self, instance: Any, owner: type | None = None) -> Any:
        if instance is None:
            return self
        return getattr(instance, self.storage_name, None)

    def __set__(self, instance: Any, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Value must be a number, got {type(value).__name__}")
        if self.min_val is not None and value < self.min_val:
            raise ValueError(f"Value {value} is below minimum allowed {self.min_val}")
        if self.max_val is not None and value > self.max_val:
            raise ValueError(f"Value {value} exceeds maximum allowed {self.max_val}")
        setattr(instance, self.storage_name, value)


class LazyProperty:
    """
    Non-data descriptor that computes a property value once and caches it in instance.__dict__.
    Subsequent access skips __get__ because instance.__dict__ overrides non-data descriptors.
    """

    def __init__(self, func: Callable[[Any], Any]) -> None:
        self.func = func
        self.__doc__ = func.__doc__

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name

    def __get__(self, instance: Any, owner: type | None = None) -> Any:
        if instance is None:
            return self
        value = self.func(instance)
        # Store result directly into instance.__dict__ so future lookups find it immediately!
        instance.__dict__[self.name] = value
        return value


class InventoryItem:
    price = BoundedNumber(min_val=0.0, max_val=10000.0)
    quantity = BoundedNumber(min_val=0, max_val=1000)

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    @LazyProperty
    def total_inventory_value(self) -> float:
        print("[COMPUTING] Calculating heavy inventory value...")
        return self.price * self.quantity


if __name__ == "__main__":
    item = InventoryItem("Laptop", 1200.0, 5)
    print(f"Price: ${item.price}, Quantity: {item.quantity}")

    # Lazy calculation fires once
    print(f"Total Value (1st call): ${item.total_inventory_value}")
    # Second access reads directly from instance.__dict__ (fast cache hit!)
    print(f"Total Value (2nd call): ${item.total_inventory_value}")
