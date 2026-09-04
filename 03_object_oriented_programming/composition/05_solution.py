"""
Topic: Composition Solutions
File: 05_solution.py
"""

class CPU:
    def __init__(self, cores: int) -> None:
        self.cores = cores


class RAM:
    def __init__(self, size_gb: int) -> None:
        self.size_gb = size_gb


class Computer:
    def __init__(self, cpu: CPU, ram: RAM) -> None:
        self.cpu = cpu
        self.ram = ram


class Author:
    def __init__(self, name: str, bio: str) -> None:
        self.name = name
        self.bio = bio


class Book:
    def __init__(self, title: str, author: Author) -> None:
        self.title = title
        self.author = author


class OrderItem:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self) -> float:
        return self.price * self.quantity


class Order:
    def __init__(self, order_id: str, items: list[OrderItem]) -> None:
        self.order_id = order_id
        self.items = items

    def calculate_total(self) -> float:
        return round(sum(item.total() for item in self.items), 2)


if __name__ == "__main__":
    print("--- Level 1 ---")
    c = Computer(CPU(8), RAM(16))
    print(f"Computer: {c.cpu.cores} CPU Cores, {c.ram.size_gb}GB RAM")

    print("\n--- Level 2 ---")
    author = Author("Martin Fowler", "Software Architect")
    book = Book("Refactoring", author)
    print(f"Book: '{book.title}' by {book.author.name}")

    print("\n--- Level 3 ---")
    items = [OrderItem("Keyboard", 89.99, 1), OrderItem("Mouse", 24.50, 2)]
    order = Order("ORD-881", items)
    print(f"Order #{order.order_id} Total: ${order.calculate_total()}")
