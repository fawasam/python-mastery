"""
Bytecode Basics: Disassembling Functions with dis.
"""

import dis


def calculate_sum(a: int, b: int) -> int:
    return a + b


def inspect_bytecode() -> None:
    print("=== Disassembled Bytecode for calculate_sum ===")
    dis.dis(calculate_sum)

    code_obj = calculate_sum.__code__
    print("\nCode Object Metadata:")
    print("Constants (co_consts):", code_obj.co_consts)
    print("Variable Names (co_varnames):", code_obj.co_varnames)


if __name__ == "__main__":
    inspect_bytecode()
