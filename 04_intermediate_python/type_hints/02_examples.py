"""
Topic: Built-in Collection Annotations
File: 02_examples.py
"""

# In Python 3.9+, use standard list, dict, set, tuple directly for type annotations!
def process_user_batch(users: list[dict[str, str | int]]) -> set[str]:
    emails = {str(u["email"]) for u in users if "email" in u}
    return emails


if __name__ == "__main__":
    batch = [
        {"name": "Alice", "email": "alice@dev.io"},
        {"name": "Bob", "email": "bob@dev.io"},
    ]
    extracted = process_user_batch(batch)
    print(f"Extracted Emails: {extracted}")
