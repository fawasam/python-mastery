"""
Topic: Lambda as Higher-Order Function Argument
File: 02_examples.py
"""

def apply_operation(val: float, op: Callable[[float], float]) -> float:
    return op(val)


if __name__ == "__main__":
    from typing import Callable

    raw_val = 100.0
    with_tax = apply_operation(raw_val, lambda x: x * 1.08)
    with_discount = apply_operation(raw_val, lambda x: x * 0.85)

    print(f"Base: ${raw_val}")
    print(f"With Tax: ${with_tax:.2f}")
    print(f"With Discount: ${with_discount:.2f}")
