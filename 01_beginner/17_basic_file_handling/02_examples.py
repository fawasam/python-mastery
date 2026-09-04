"""
Topic: Modern pathlib Utilities & Search
File: 02_examples.py
"""
from pathlib import Path

def demonstrate_pathlib_features() -> None:
    current_dir = Path(__file__).parent
    print(f"Current Directory: {current_dir}")
    print(f"Directory Name:   {current_dir.name}")
    print(f"Parent Directory:  {current_dir.parent.name}")

    # Searching directory for python files using glob()
    print("\n--- Python files in current topic directory ---")
    py_files = list(current_dir.glob("*.py"))
    for py_file in py_files:
        size_bytes = py_file.stat().st_size
        print(f"  - {py_file.name:<25} ({size_bytes} bytes)")


if __name__ == "__main__":
    demonstrate_pathlib_features()
