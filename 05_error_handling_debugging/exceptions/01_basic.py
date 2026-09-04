"""
Basic Exception Handling with try-except-else-finally.
"""


def safe_divide(a: float, b: float) -> float | None:
    """
    Divides 'a' by 'b' with complete error handling semantics.
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"[ERROR] Cannot divide by zero: {e}")
    except TypeError as e:
        print(f"[ERROR] Invalid numeric type: {e}")
    else:
        # 'else' executes only if try block completes without any exception
        print(f"[SUCCESS] {a} / {b} = {result}")
    finally:
        # 'finally' runs unconditionally for resource cleanup
        print("[CLEANUP] Division attempt finalized.")

    return result


if __name__ == "__main__":
    print("--- Attempt 1: Valid Division ---")
    safe_divide(10.0, 2.0)

    print("\n--- Attempt 2: Zero Division ---")
    safe_divide(10.0, 0.0)
