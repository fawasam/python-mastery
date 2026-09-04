"""
Topic: Variables & Dynamic Typing
File: 01_basic.py

This script demonstrates:
1. Creating variables using snake_case convention
2. Understanding variables as references to memory locations
3. Checking object type and memory address using type() and id()
"""

def demonstrate_variables() -> None:
    # 1. Variable creation & assignment
    # In Python, we do not specify explicit types like 'int' or 'string'.
    # We assign values directly, and Python binds the variable name to the object.
    user_age: int = 25
    user_name: str = "Sophia"
    account_balance: float = 1250.75
    is_premium_member: bool = True

    print("--- User Profile ---")
    print("Name:", user_name)
    print("Age:", user_age)
    print("Balance: $", account_balance)
    print("Premium:", is_premium_member)

    # 2. Dynamic Typing
    # A single variable name can point to different object types over time.
    current_status = "Pending"
    print("\nInitial status type:", type(current_status))

    # Reassigning current_status to an integer code
    current_status = 200
    print("Updated status type:", type(current_status))


if __name__ == "__main__":
    demonstrate_variables()
