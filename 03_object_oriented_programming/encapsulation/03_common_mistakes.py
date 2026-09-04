"""
Topic: Common Mistakes with Encapsulation
File: 03_common_mistakes.py
"""

def mistake_1_expecting_private_to_be_truly_inaccessible() -> None:
    # ❌ WRONG: Believing `__private` attributes cannot be accessed externally in Python.
    # Python uses name mangling (_ClassName__attribute), NOT strict compiler enforcement!
    
    # ✅ CORRECT: Double underscore `__` is meant to prevent accidental name collisions in subclasses, NOT to protect against malicious security attacks.
    print("Name mangling prevents accidental subclass attribute collisions, not malicious access.")


if __name__ == "__main__":
    mistake_1_expecting_private_to_be_truly_inaccessible()
