"""
Topic: Common Mistakes with Input & Output
File: 03_common_mistakes.py
"""

def mistake_1_adding_str_input_directly() -> None:
    # ❌ WRONG:
    # num1 = input("Enter number 1: ") # returns "5"
    # num2 = input("Enter number 2: ") # returns "10"
    # result = num1 + num2 # returns string concatenation "510" instead of 15!
    
    # ✅ CORRECT: Explicitly convert to int or float
    num1 = int("5")
    num2 = int("10")
    result = num1 + num2
    print(f"Correct addition result: {result}")


def mistake_2_f_string_expression_side_effects() -> None:
    # f-strings allow expressions inside {}, but putting heavy logic or mutating operations
    # inside f-strings makes code hard to debug.
    
    # ❌ WRONG (unclean):
    # print(f"Status: {data.update({'key': 'val'}) or data}")
    
    # ✅ CORRECT: Compute result beforehand, then format.
    status = "Active"
    print(f"Status: {status}")


if __name__ == "__main__":
    mistake_1_adding_str_input_directly()
    mistake_2_f_string_expression_side_effects()
