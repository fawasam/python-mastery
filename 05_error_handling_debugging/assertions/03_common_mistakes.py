"""
Common Mistakes with Python Assertions.
"""


# MISTAKE 1: Using parenthesized tuples in assertion statements
def mistake_tuple_assertion() -> None:
    x = -10
    # DANGER: In Python, assert (x > 0, "Message") evaluates bool((x > 0, "Message")),
    # which is a non-empty tuple -> ALWAYS TRUTHY! The assertion NEVER fires!
    assert (x > 0, "x must be positive")  # DANGEROUS BUG!


# GOOD PRACTICE: No parentheses around condition and message
def good_assertion() -> None:
    x = -10
    assert x > 0, "x must be positive"


if __name__ == "__main__":
    print("--- Demonstrating Mistake 1 (Tuple Assertion Bug) ---")
    mistake_tuple_assertion()  # Passes silently even though x = -10!
    print("Tuple assertion unexpectedly PASSED because (False, 'Message') is a truthy tuple!")

    print("\n--- Demonstrating Good Assertion ---")
    try:
        good_assertion()
    except AssertionError as e:
        print(f"Good assertion correctly FIRED with message: {e}")
