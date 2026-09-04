"""
Topic: Common Mistakes with Context Managers
File: 03_common_mistakes.py
"""

def mistake_1_suppressing_exceptions_accidentally() -> None:
    # ❌ WRONG: Returning True in __exit__ swallows ALL exceptions inside the block silently!
    class SilentSuppressor:
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            print(f"Swallowing exception silently: {exc_val}")
            return True  # Returning True suppresses error propagation!

    with SilentSuppressor():
        result = 10 / 0  # ZeroDivisionError is swallowed!
    print("Execution continued after swallowed ZeroDivisionError!")


if __name__ == "__main__":
    mistake_1_suppressing_exceptions_accidentally()
