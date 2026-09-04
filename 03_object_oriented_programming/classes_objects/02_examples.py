"""
Topic: Instance Attributes vs Class Attributes
File: 02_examples.py
"""

class Employee:
    # Class attribute
    company_name = "Tech Corp"

    def __init__(self, emp_id: int, name: str) -> None:
        self.emp_id = emp_id
        self.name = name


if __name__ == "__main__":
    e1 = Employee(1, "Alice")
    e2 = Employee(2, "Bob")

    print(f"e1 company: {e1.company_name} | e2 company: {e2.company_name}")

    # Modifying class attribute on class changes it for ALL instances
    Employee.company_name = "Global Tech Corp"
    print(f"Updated e1 company: {e1.company_name} | e2 company: {e2.company_name}")
