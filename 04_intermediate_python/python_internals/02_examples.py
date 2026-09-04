"""
Comparing Bytecode Execution: Local Variable Lookup vs Global/Attribute Lookup.
"""

import dis
import math

GLOBAL_VAL = 100.0


def use_global(x: float) -> float:
    # LOAD_GLOBAL requires dictionary lookup in globals dict
    return x + GLOBAL_VAL


def use_local(x: float) -> float:
    # Local variable is stored in C-array; accessed instantly via LOAD_FAST index offset
    local_val = 100.0
    return x + local_val


if __name__ == "__main__":
    print("--- Bytecode for Global Variable Access ---")
    dis.dis(use_global)

    print("\n--- Bytecode for Local Variable Access ---")
    dis.dis(use_local)
