"""
Topic: Common Import Mistakes
File: 03_common_mistakes.py
"""

def mistake_1_wildcard_imports() -> None:
    # ❌ WRONG: from math import *
    # Wildcard imports pollute the local namespace and obscure where functions originate!
    
    # ✅ CORRECT: Explicit imports or namespace qualification
    import math
    print(f"Explicit qualification: {math.cos(0)}")


def mistake_2_naming_file_same_as_standard_library() -> None:
    # ❌ WRONG: Creating a local file named `random.py` or `math.py`!
    # When you type `import random`, Python finds your local `random.py` first!
    # This triggers an AttributeError when calling standard functions like `random.randint()`.

    # ✅ CORRECT: Name custom script files uniquely (e.g. `random_utils.py`).
    print("Always avoid naming local scripts identical to built-in modules.")


if __name__ == "__main__":
    mistake_1_wildcard_imports()
    mistake_2_naming_file_same_as_standard_library()
