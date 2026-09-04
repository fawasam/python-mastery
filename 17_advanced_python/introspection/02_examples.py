"""
Advanced Introspection: Function Signature and Parameter Inspection with inspect.
"""

import inspect
from typing import Any


def calculate_tax(amount: float, tax_rate: float = 0.05) -> float:
    """Calculate tax for transaction amount."""
    return amount * tax_rate


def inspect_function_contract(func: Any) -> None:
    sig = inspect.signature(func)
    print(f"Function Name: {func.__name__}")
    print(f"Docstring: {func.__doc__}")
    print(f"Return Annotation: {sig.return_annotation}")
    print("Parameters:")
    for p_name, p_obj in sig.parameters.items():
        print(f" - {p_name}: type={p_obj.annotation}, default={p_obj.default}")


if __name__ == "__main__":
    inspect_function_contract(calculate_tax)
