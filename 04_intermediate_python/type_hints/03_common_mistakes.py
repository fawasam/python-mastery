"""
Topic: Common Mistakes with Type Hints
File: 03_common_mistakes.py
"""

def mistake_1_expecting_type_hints_to_enforce_runtime_types() -> None:
    # ❌ WRONG: Expecting Python runtime to raise TypeError at execution time if a wrong type is passed!
    # Type hints in Python are NOT enforced at runtime by default—they are consumed by static type checkers like mypy!
    
    # ✅ CORRECT: Use runtime validation libraries (like Pydantic) or explicit isinstance() checks if runtime enforcement is required.
    print("Type hints are for IDEs and mypy static analysis, not runtime enforcement.")


if __name__ == "__main__":
    mistake_1_expecting_type_hints_to_enforce_runtime_types()
