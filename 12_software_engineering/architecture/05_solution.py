"""
Solutions: Architecture Exercises.
"""

from dataclasses import dataclass
from typing import Protocol


@dataclass
class Product:
    product_id: str
    name: str
    price: float


class ProductRepository(Protocol):
    def save(self, product: Product) -> None:
        ...
        
    def find_by_id(self, product_id: str) -> Product | None:
        ...


class InMemoryProductRepository:
    def __init__(self) -> None:
        self._store: dict[str, Product] = {}

    def save(self, product: Product) -> None:
        self._store[product.product_id] = product

    def find_by_id(self, product_id: str) -> Product | None:
        return self._store.get(product_id)


class ProductService:
    def __init__(self, repo: ProductRepository) -> None:
        self.repo = repo

    def create_product(self, product_id: str, name: str, price: float) -> Product:
        if price <= 0:
            raise ValueError("Price must be greater than zero")
            
        prod = Product(product_id=product_id, name=name, price=price)
        self.repo.save(prod)
        return prod


if __name__ == "__main__":
    repo = InMemoryProductRepository()
    service = ProductService(repo)
    p = service.create_product("P-101", "Keyboard", 79.99)
    print("Created Product:", p)
