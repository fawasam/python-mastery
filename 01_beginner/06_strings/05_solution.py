"""
Topic: String Solutions
File: 05_solution.py
"""

def level_1_easy() -> None:
    text = "python programming"
    result = text.title()
    print(f"Title cased: '{result}'")


def level_2_medium(s: str) -> bool:
    clean = "".join(s.lower().split())
    is_pal = clean == clean[::-1]
    print(f"Is '{s}' a palindrome? {is_pal}")
    return is_pal


def level_3_hard(email: str) -> str:
    clean_email = email.strip()
    if "@" in clean_email:
        domain = clean_email.split("@")[-1]
        print(f"Email: '{email}' -> Domain: '{domain}'")
        return domain
    raise ValueError("Invalid email format")


def level_4_real_world(card_number: str) -> str:
    digits_only = "".join(c for c in card_number if c.isdigit())
    if len(digits_only) < 4:
        raise ValueError("Invalid card number length")
    last_four = digits_only[-4:]
    masked = "XXXX-XXXX-XXXX-" + last_four
    print(f"Card: '{card_number}' -> Masked: '{masked}'")
    return masked


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium("A man a plan a canal Panama")
    level_2_medium("Hello World")

    print("\n--- Level 3 ---")
    level_3_hard("  john.doe@company.org  ")

    print("\n--- Level 4 ---")
    level_4_real_world("4532 8901 2345 9812")
