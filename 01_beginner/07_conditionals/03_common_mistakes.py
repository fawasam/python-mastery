"""
Topic: Common Mistakes with Conditionals
File: 03_common_mistakes.py
"""

def mistake_1_using_if_instead_of_elif() -> None:
    score = 95

    # ❌ WRONG: Independent if statements execute ALL checks!
    # Even if score >= 90 is True, score >= 80 will also execute and overwrite grade!
    grade = "F"
    if score >= 90:
        grade = "A"
    if score >= 80:  # Executes even though score is 95!
        grade = "B"
    print(f"Buggy grade (used independent if): {grade}")

    # ✅ CORRECT: Use elif so only the first matching branch executes!
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    print(f"Correct grade (used elif): {grade}")


def mistake_2_redundant_boolean_comparisons() -> None:
    is_active = True
    
    # ❌ UNNECESSARY: if is_active == True:
    # ✅ CLEAN:
    if is_active:
        print("User is active")


if __name__ == "__main__":
    mistake_1_using_if_instead_of_elif()
    mistake_2_redundant_boolean_comparisons()
