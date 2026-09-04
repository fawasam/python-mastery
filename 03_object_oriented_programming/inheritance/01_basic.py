"""
Topic: Single Inheritance & super() Basics
File: 01_basic.py
"""

class Employee:
    def __init__(self, emp_id: int, name: str, salary: float) -> None:
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def get_details(self) -> str:
        return f"[{self.emp_id}] {self.name} - ${self.salary:,.2f}"


class Developer(Employee):
    def __init__(self, emp_id: int, name: str, salary: float, programming_language: str) -> None:
        # Call parent initializer using super()
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    def get_details(self) -> str:
        # Override parent method and extend description
        parent_details = super().get_details()
        return f"{parent_details} (Dev: {self.programming_language})"


if __name__ == "__main__":
    dev = Developer(101, "Alice", 120000.0, "Python")
    print(dev.get_details())
