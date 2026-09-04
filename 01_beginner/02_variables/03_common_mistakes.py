"""
Topic: Variables & Naming Anti-Patterns
File: 03_common_mistakes.py

Common pitfalls when defining and using variables in Python.
"""

def mistake_1_using_keywords() -> None:
    # ❌ WRONG: class = "Computer Science"
    # 'class' is a reserved Python keyword.
    
    # ✅ CORRECT:
    course_class = "Computer Science"
    print("Class variable:", course_class)


def mistake_2_unbound_variable() -> None:
    # ❌ WRONG: print(total_score) before total_score is created.
    # Causes a NameError: name 'total_score' is not defined.
    
    # ✅ CORRECT: Define before reading
    total_score = 100
    print("Total score:", total_score)


def mistake_3_confusing_equality_and_assignment() -> None:
    # ❌ WRONG: if x = 5: (Single '=' is assignment, not comparison)
    # Causes SyntaxError in Python.
    
    # ✅ CORRECT: Use '==' for checking equality, '=' for storing a value.
    x = 5
    if x == 5:
        print("x is equal to 5")


if __name__ == "__main__":
    mistake_1_using_keywords()
    mistake_2_unbound_variable()
    mistake_3_confusing_equality_and_assignment()
