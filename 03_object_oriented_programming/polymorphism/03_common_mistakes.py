"""
Topic: Common Mistakes with Polymorphism
File: 03_common_mistakes.py
"""

def mistake_1_type_checking_instead_of_duck_typing() -> None:
    # ❌ WRONG: Explicit type checking defeats duck typing!
    # if isinstance(obj, StripeGateway): ... elif isinstance(obj, PayPalGateway): ...

    # ✅ CORRECT: Call the target method directly or use AttributeError handling / Protocols!
    print("Embrace duck typing: Call methods directly rather than using isinstance checks.")


if __name__ == "__main__":
    mistake_1_type_checking_instead_of_duck_typing()
