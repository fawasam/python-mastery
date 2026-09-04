"""
Common Mistakes in Exception Handling.
"""


# MISTAKE 1: Bare 'except:' clause
def bad_bare_except() -> None:
    try:
        # Imagine user presses Ctrl+C here or SystemExit occurs
        val = int("abc")
    except:  # BAD! Catches KeyboardInterrupt, SystemExit, and hides bugs
        print("Something failed!")


# MISTAKE 2: Silent exception swallowing
def bad_swallowing() -> None:
    try:
        data = {"key": "value"}
        val = data["missing_key"]
    except KeyError:
        pass  # BAD! Silent failure hides structural bugs


# GOOD PRACTICE: Specific exception handling with logging/recovery
def good_exception_handling() -> None:
    try:
        data = {"key": "value"}
        val = data["missing_key"]
    except KeyError as e:
        print(f"[RECOVERY] Key {e} not found in dictionary, using fallback default.")
        val = "default_value"


if __name__ == "__main__":
    print("--- Demonstrating Good Exception Handling ---")
    good_exception_handling()
