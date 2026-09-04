"""
Topic: Common Scope Mistakes (UnboundLocalError & Shadowing)
File: 03_common_mistakes.py
"""

total_points = 100

def mistake_1_unbound_local_error() -> None:
    # ❌ WRONG: Modifying global variable without `global` keyword!
    # total_points += 10
    # UnboundLocalError: local variable 'total_points' referenced before assignment

    # ✅ CORRECT: Declare global explicitly if mutating primitive
    global total_points
    total_points += 10
    print(f"Correctly updated global total_points: {total_points}")


def mistake_2_shadowing_built_in_names() -> None:
    # ❌ WRONG: Defining a variable with built-in function names like 'list', 'str', 'len', 'sum'
    # list = [1, 2, 3] # Shadows built-in list function!
    # new_items = list("abc") # Crashes because 'list' is now a list object, not the built-in function!

    # ✅ CORRECT: Use distinct names
    my_list = [1, 2, 3]
    converted = list("abc")
    print(f"Built-in list function preserved: {converted}")


if __name__ == "__main__":
    mistake_1_unbound_local_error()
    mistake_2_shadowing_built_in_names()
