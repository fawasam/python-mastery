"""
Topic: Regex Basics with re Module
File: 01_basic.py
"""
import re

def demonstrate_regex_basics() -> None:
    text = "Order #10042 processed for user alex@dev.io on 2026-09-04."

    # 1. Searching for single match
    match = re.search(r"#\d+", text)
    if match:
        print(f"Found order number: {match.group()}")

    # 2. Finding all email addresses
    emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    print(f"Extracted emails: {emails}")

    # 3. Replacing text using re.sub()
    anonymized = re.sub(r"[\w\.-]+@[\w\.-]+\.\w+", "[REDACTED]", text)
    print(f"Anonymized text: {anonymized}")


if __name__ == "__main__":
    demonstrate_regex_basics()
