"""
Topic: Common Mistakes with Regex
File: 03_common_mistakes.py
"""

def mistake_1_raw_strings_missing() -> None:
    # ❌ WRONG: Not using raw string r"..." means \b or \d might be interpreted as backspace!
    # pattern = "\bword\b"

    # ✅ CORRECT: Always use raw string prefixes r"..." for regex patterns!
    pattern = r"\bword\b"
    print(f"Raw string pattern: {pattern}")


def mistake_2_greedy_vs_non_greedy() -> None:
    # Greedy `.*` matches as MUCH as possible!
    text = "<div>First</div><div>Second</div>"
    greedy_match = re.findall(r"<div>.*</div>", text)
    print(f"Greedy match:     {greedy_match}")  # Matches entire text!

    # Non-greedy `.*?` matches as LITTLE as possible!
    non_greedy = re.findall(r"<div>.*?</div>", text)
    print(f"Non-greedy match: {non_greedy}")  # Matches each div separately!


if __name__ == "__main__":
    import re
    mistake_1_raw_strings_missing()
    mistake_2_greedy_vs_non_greedy()
