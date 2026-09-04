"""
Advanced Bytecode: Comparing Opcode Instructions of List Comp vs Loop.
"""

import dis


def list_comp_method(items: list[int]) -> list[int]:
    return [x * 2 for x in items]


def loop_method(items: list[int]) -> list[int]:
    result = []
    for x in items:
        result.append(x * 2)
    return result


def compare_opcodes() -> None:
    print("=== List Comprehension Opcodes ===")
    dis.dis(list_comp_method)

    print("\n=== Loop Method Opcodes ===")
    dis.dis(loop_method)


if __name__ == "__main__":
    compare_opcodes()
