"""
Basic Python Internals: Disassembling Functions and Inspecting Code Objects.
"""

import dis


def compute_total(price: float, tax_rate: float) -> float:
    """Calculates total price including tax."""
    tax = price * tax_rate
    total = price + tax
    return total


def inspect_code_object() -> None:
    code = compute_total.__code__
    print(f"Function Name: {code.co_name}")
    print(f"Argument Count: {code.co_argcount}")
    print(f"Local Variable Names (co_varnames): {code.co_varnames}")
    print(f"Constants (co_consts): {code.co_consts}")


if __name__ == "__main__":
    print("--- Inspecting Function Code Object Metadata ---")
    inspect_code_object()

    print("\n--- Disassembling 'compute_total' Bytecode ---")
    dis.dis(compute_total)
