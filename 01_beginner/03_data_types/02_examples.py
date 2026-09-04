"""
Topic: Type Casting & Truthiness Examples
File: 02_examples.py
"""

def demonstrate_type_conversion() -> None:
    # 1. Converting String to Integer and Float
    numeric_str = "42"
    float_str = "3.14159"

    converted_int = int(numeric_str)
    converted_float = float(float_str)
    print(f"int('42') -> {converted_int} ({type(converted_int)})")
    print(f"float('3.14159') -> {converted_float} ({type(converted_float)})")

    # 2. Converting Numbers to String
    age = 30
    price = 19.99
    formatted = "User is " + str(age) + " years old. Product costs $" + str(price)
    print(formatted)

    # 3. Truthiness Evaluation
    print("\n--- Truthiness Evaluation ---")
    sample_values = [0, 1, "", "Python", [], [1, 2], None, True, False]
    for val in sample_values:
        print(f"bool({repr(val):<10}) -> {bool(val)}")


if __name__ == "__main__":
    demonstrate_type_conversion()
