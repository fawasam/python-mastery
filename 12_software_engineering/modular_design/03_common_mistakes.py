"""
Modular Design Pitfalls: Circular Imports.
"""

# MISTAKE: Circular imports (Module A imports Module B while Module B imports Module A at top level).
# FIX:
# 1. Use type checking imports: `if TYPE_CHECKING: import B`
# 2. Extract shared interfaces/dataclasses into a separate common/types module.
# 3. Perform inline imports inside functions when strictly necessary.

if __name__ == "__main__":
    print("Circular import mitigation rules analyzed.")
