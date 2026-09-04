"""
Topic: Hello World & Printing Basics
File: 03_common_mistakes.py

This file demonstrates common beginner mistakes when writing Python code,
explaining WHY they fail and HOW to fix them properly.
"""

def mistake_1_case_sensitivity() -> None:
    # ❌ WRONG: Print("Hello World")
    # Explanation: Python is case-sensitive. 'Print' with a capital 'P' is not recognized
    # because the built-in function is lowercase 'print'.
    
    # ✅ CORRECT:
    print("Correct function casing: print()")


def mistake_2_unquoted_string() -> None:
    # ❌ WRONG: print(Hello World)
    # Explanation: Without quotation marks, Python thinks 'Hello' is a variable name.
    
    # ✅ CORRECT:
    print("Strings must always be enclosed in quotation marks.")


def mistake_3_mismatched_quotes() -> None:
    # ❌ WRONG: print("Hello World')
    # Explanation: Opening double quote must be closed with double quote. Mismatched quotes
    # cause a SyntaxError (unterminated string literal).
    
    # ✅ CORRECT:
    print("Quotes must match on both ends.")


if __name__ == "__main__":
    print("--- Demonstrating Corrected Syntax ---")
    mistake_1_case_sensitivity()
    mistake_2_unquoted_string()
    mistake_3_mismatched_quotes()
