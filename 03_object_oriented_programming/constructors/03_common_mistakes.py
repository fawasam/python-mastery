"""
Topic: Common Mistakes with Constructors
File: 03_common_mistakes.py
"""

def mistake_1_returning_value_from_init() -> None:
    class BadInit:
        def __init__(self) -> None:
            # ❌ WRONG: return "hello"
            # TypeError: __init__() should return None, not 'str'
            pass

    print("Remember: __init__ must ALWAYS return None.")


if __name__ == "__main__":
    mistake_1_returning_value_from_init()
