"""
Topic: Classes Solutions
File: 05_solution.py
"""

class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self) -> str:
        return f"'{self.title}' by {self.author} ({self.pages} pages)"


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance


class Student:
    def __init__(self, name: str) -> None:
        self.name = name
        self.grades: list[float] = []

    def add_grade(self, grade: float) -> None:
        if 0 <= grade <= 100:
            self.grades.append(grade)

    def get_average(self) -> float:
        return sum(self.grades) / len(self.grades) if self.grades else 0.0


class InventoryItem:
    def __init__(self, sku: str, name: str, price: float, quantity: int) -> None:
        self.sku = sku
        self.name = name
        self.price = price
        self.quantity = quantity

    def restock(self, qty: int) -> int:
        self.quantity += qty
        return self.quantity

    def calculate_total_value(self) -> float:
        return round(self.price * self.quantity, 2)


if __name__ == "__main__":
    print("--- Level 1 ---")
    b = Book("Clean Code", "Robert C. Martin", 464)
    print(b.summary())

    print("\n--- Level 2 ---")
    acc = BankAccount("Alice", 100.0)
    acc.deposit(50.0)
    acc.withdraw(30.0)
    print(f"Account Balance: ${acc.balance}")

    print("\n--- Level 3 ---")
    st = Student("Bob")
    st.add_grade(90)
    st.add_grade(80)
    print(f"Student average: {st.get_average()}")

    print("\n--- Level 4 ---")
    item = InventoryItem("SKU-9901", "Gaming Monitor", 299.99, 10)
    print(f"Inventory total value: ${item.calculate_total_value()}")
