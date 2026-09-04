"""
Topic: Exception Handling Basics
File: 01_basic.py
"""

def safe_divide(numerator: float, denominator: float) -> float | None:
    try:
        print(f"Attempting division: {numerator} / {denominator}")
        result = numerator / denominator
    except ZeroDivisionError as err:
        print(f"❌ Handled ZeroDivisionError: {err}")
        return None
    except TypeError as err:
        print(f"❌ Handled TypeError: {err}")
        return None
    else:
        print(f"✅ Calculation successful: {result}")
        return result
    finally:
        print("  [Cleanup] Execution pass complete.\n")


if __name__ == "__main__":
    safe_divide(10.0, 2.0)
    safe_divide(10.0, 0.0)
