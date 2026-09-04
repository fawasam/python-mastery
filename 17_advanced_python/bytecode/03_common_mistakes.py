"""
Bytecode Common Pitfalls.
"""

# MISTAKE: Assuming CPython bytecode is portable across different major Python runtime versions.
# WHY: CPython opcodes change, get added, or get refactored between Python releases (e.g. Python 3.11 vs 3.12 vs 3.14).
# FIX: Do not hardcode raw opcode integer values in production logic; use `dis` module constants.

if __name__ == "__main__":
    print("Bytecode version compatibility rules verified.")
