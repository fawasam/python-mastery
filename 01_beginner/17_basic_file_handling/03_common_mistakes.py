"""
Topic: Common File Handling Mistakes
File: 03_common_mistakes.py
"""

def mistake_1_forgetting_to_close_file() -> None:
    # ❌ WRONG: f = open("data.txt", "w") -> if exception occurs before f.close(), file remains locked!
    
    # ✅ CORRECT: Always use `with open(...)` context manager
    print("Always use 'with open()' context manager for deterministic file closing.")


def mistake_2_reading_huge_file_with_read() -> None:
    # ❌ WRONG: content = file.read() on a 10GB log file loads the ENTIRE file into RAM, triggering MemoryError!

    # ✅ CORRECT: Iterate line-by-line using `for line in file:` which streams data in chunks.
    print("Stream large files line-by-line rather than calling file.read() all at once.")


if __name__ == "__main__":
    mistake_1_forgetting_to_close_file()
    mistake_2_reading_huge_file_with_read()
