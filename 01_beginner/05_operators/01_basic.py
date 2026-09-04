"""
Topic: Python Operators Overview
File: 01_basic.py
"""

def demonstrate_arithmetic_operators() -> None:
    a = 15
    b = 4

    print(f"a = {a}, b = {b}")
    print(f"Addition (a + b):         {a + b}")
    print(f"Subtraction (a - b):      {a - b}")
    print(f"Multiplication (a * b):   {a * b}")
    print(f"Float Division (a / b):   {a / b}")    # Always returns a float
    print(f"Floor Division (a // b):  {a // b}")   # Truncates decimal
    print(f"Modulus (a % b):          {a % b}")    # Remainder
    print(f"Exponentiation (a ** b):  {a ** b}")   # 15 to the power of 4


def demonstrate_logical_and_membership() -> None:
    is_logged_in = True
    is_admin = False
    
    # Short-circuit logical evaluation
    can_access_dashboard = is_logged_in and (is_admin or True)
    print(f"\nCan access dashboard: {can_access_dashboard}")

    # Membership operator
    allowed_roles = ["admin", "super_user", "editor"]
    current_role = "editor"
    print(f"Is '{current_role}' in allowed roles? {current_role in allowed_roles}")


if __name__ == "__main__":
    print("--- Arithmetic Operators ---")
    demonstrate_arithmetic_operators()
    
    print("\n--- Logical & Membership Operators ---")
    demonstrate_logical_and_membership()
