"""
Topic: String Slicing & Common Methods
File: 01_basic.py
"""

def demonstrate_string_slicing() -> None:
    message = "Python Software Engineering"

    # 1. Indexing
    print(f"Original: '{message}'")
    print(f"First character (message[0]): '{message[0]}'")
    print(f"Last character (message[-1]): '{message[-1]}'")

    # 2. Slicing [start:stop:step]
    print(f"\nSlice [0:6]: '{message[0:6]}'")
    print(f"Slice [7:15]: '{message[7:15]}'")
    print(f"Slice from start to 6 [:6]: '{message[:6]}'")
    print(f"Slice from 16 to end [16:]: '{message[16:]}'")
    print(f"Reverse string [::-1]: '{message[::-1]}'")

    # 3. String Methods
    raw_email = "   User.Name@Domain.Com   "
    clean_email = raw_email.strip().lower()
    print(f"\nRaw email:   '{raw_email}'")
    print(f"Clean email: '{clean_email}'")


if __name__ == "__main__":
    demonstrate_string_slicing()
