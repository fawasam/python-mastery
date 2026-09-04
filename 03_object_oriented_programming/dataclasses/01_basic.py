"""
Topic: Dataclass Fundamentals & Post-Init Validation
File: 01_basic.py
"""
from dataclasses import dataclass, field

@dataclass
class Product:
    sku: str
    name: str
    price: float
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError(f"Price cannot be negative: {self.price}")
        self.sku = self.sku.upper()


if __name__ == "__main__":
    p1 = Product(sku="sku-100", name="Wireless Mouse", price=29.99, tags=["electronics"])
    p2 = Product(sku="sku-100", name="Wireless Mouse", price=29.99, tags=["electronics"])

    print(f"Product: {p1}")
    print(f"Automatic __eq__ comparison (p1 == p2): {p1 == p2}")
