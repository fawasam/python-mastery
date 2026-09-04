"""
Topic: File I/O & pathlib Basics
File: 01_basic.py
"""
from pathlib import Path

def demonstrate_file_operations() -> None:
    target_file = Path(__file__).parent / "sample_output.txt"

    # 1. Writing to a file using context manager
    print(f"Writing to file: {target_file.name}")
    with target_file.open("w", encoding="utf-8") as f:
        f.write("Line 1: System Online\n")
        f.write("Line 2: Processing batch job\n")

    # 2. Appending to a file
    with target_file.open("a", encoding="utf-8") as f:
        f.write("Line 3: Batch completed successfully\n")

    # 3. Reading line-by-line (Memory Efficient)
    print("\n--- Reading file contents ---")
    with target_file.open("r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, 1):
            print(f"[{line_num}] {line.strip()}")

    # Cleanup temporary test file
    if target_file.exists():
        target_file.unlink()
        print(f"\nCleaned up temp file: {target_file.name}")


if __name__ == "__main__":
    demonstrate_file_operations()
