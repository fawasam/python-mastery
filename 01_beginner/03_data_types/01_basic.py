"""
Topic: Scalar Data Types & Type Checking
File: 01_basic.py

Demonstrates primitive types in Python: int, float, str, bool, and NoneType.
"""

def demonstrate_scalar_types() -> None:
    # 1. Integer (arbitrary precision in Python 3)
    item_count: int = 1_000_000  # Underscores enhance readability for large integers
    print(f"item_count = {item_count} (type: {type(item_count).__name__})")

    # 2. Float (floating point representation)
    cpu_usage_percent: float = 45.85
    print(f"cpu_usage_percent = {cpu_usage_percent} (type: {type(cpu_usage_percent).__name__})")

    # 3. String (Unicode characters)
    status_message: str = "System Online"
    print(f"status_message = '{status_message}' (type: {type(status_message).__name__})")

    # 4. Boolean (True or False)
    is_healthy: bool = True
    print(f"is_healthy = {is_healthy} (type: {type(is_healthy).__name__})")

    # 5. NoneType (represents absence of value)
    last_error: None = None
    print(f"last_error = {last_error} (type: {type(last_error).__name__})")


if __name__ == "__main__":
    demonstrate_scalar_types()
