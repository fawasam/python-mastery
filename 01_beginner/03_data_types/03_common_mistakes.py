"""
Topic: Common Mistakes in Data Types & Casting
File: 03_common_mistakes.py
"""

def mistake_1_string_integer_concatenation() -> None:
    # ❌ WRONG: result = "Age: " + 25
    # TypeError: can only concatenate str (not "int") to str
    
    # ✅ CORRECT: Explicit conversion or f-string
    result = "Age: " + str(25)
    print(result)


def mistake_2_invalid_string_conversion() -> None:
    # ❌ WRONG: val = int("hello")
    # ValueError: invalid literal for int() with base 10: 'hello'
    
    # ✅ CORRECT: Validate string before casting or handle exceptions
    raw_input = "hello"
    if raw_input.isdigit():
        val = int(raw_input)
        print("Converted:", val)
    else:
        print(f"Cannot convert '{raw_input}' to integer safely.")


def mistake_3_float_precision_expectations() -> None:
    # Floating-point representation in binary causes tiny precision quirks:
    # 0.1 + 0.2 == 0.30000000000000004 != 0.3
    
    val1 = 0.1 + 0.2
    print(f"0.1 + 0.2 = {val1}")
    print(f"0.1 + 0.2 == 0.3 is {val1 == 0.3}")
    
    # ✅ CORRECT: Use math.isclose() or round() when comparing floats
    import math
    print(f"math.isclose(0.1 + 0.2, 0.3) is {math.isclose(val1, 0.3)}")


if __name__ == "__main__":
    mistake_1_string_integer_concatenation()
    mistake_2_invalid_string_conversion()
    mistake_3_float_precision_expectations()
