"""
Topic: Lambda Basics & Custom Key Sorting
File: 01_basic.py
"""

def demonstrate_lambda() -> None:
    # 1. Simple inline lambda
    add = lambda a, b: a + b
    print(f"Lambda add(10, 20): {add(10, 20)}")

    # 2. Sorting list of dictionaries by key
    employees = [
        {"name": "Alice", "salary": 95000},
        {"name": "Bob", "salary": 62000},
        {"name": "Charlie", "salary": 110000},
    ]

    # Sort descending by salary using lambda key extractor
    sorted_emp = sorted(employees, key=lambda emp: emp["salary"], reverse=True)
    print("\nEmployees sorted by salary descending:")
    for emp in sorted_emp:
        print(f"  - {emp['name']}: ${emp['salary']:,}")


if __name__ == "__main__":
    demonstrate_lambda()
