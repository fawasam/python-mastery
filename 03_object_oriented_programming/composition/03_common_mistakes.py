"""
Topic: Common Mistakes (Overusing Inheritance instead of Composition)
File: 03_common_mistakes.py
"""

def mistake_1_fragile_base_class_inheritance() -> None:
    # ❌ WRONG: Subclassing a complex class just to reuse a single helper function creates rigid coupling!
    # class OrderProcessor(DatabaseConnection): ... (OrderProcessor IS NOT A DatabaseConnection!)

    # ✅ CORRECT: Use composition! Pass DatabaseConnection as a component HAS-A dependency.
    print("Rule of thumb: Inherit only when true 'Is-A' relationship exists; use composition for everything else.")


if __name__ == "__main__":
    mistake_1_fragile_base_class_inheritance()
