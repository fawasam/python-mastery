"""
Topic: Common Mistakes with Strings
File: 03_common_mistakes.py
"""

def mistake_1_string_mutation_attempt() -> None:
    # ❌ WRONG: Attempting to modify character by index
    # text = "Python"
    # text[0] = "p" -> TypeError: 'str' object does not support item assignment
    
    # ✅ CORRECT: Strings are immutable! Create a new string using slicing or replace()
    text = "Python"
    updated_text = "p" + text[1:]
    print(f"Updated text: {updated_text}")


def mistake_2_forgetting_return_value_of_string_methods() -> None:
    # ❌ WRONG:
    # message = "  hello world  "
    # message.strip() # Does NOT change message in place!
    # print(message) # Still prints "  hello world  "
    
    # ✅ CORRECT: String methods return a NEW string. Reassign the result!
    message = "  hello world  "
    message = message.strip()
    print(f"Stripped message: '{message}'")


if __name__ == "__main__":
    mistake_1_string_mutation_attempt()
    mistake_2_forgetting_return_value_of_string_methods()
