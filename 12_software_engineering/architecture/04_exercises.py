"""
Exercises: Building Layered Clean Architecture Components.
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


class ProductService:
    """
    Exercise: Implement ProductService with repository injection to handle product registration.
    
    Level 2 - Medium
    """
    def __init__(self, repo: ProductRepository) -> None:
        raise NotImplementedError("Implement ProductService constructor")

    def create_product(self, product_id: str, name: str, price: float) -> Product:
        raise NotImplementedError("Implement create_product method with validation")
