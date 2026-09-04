"""
Topic: Recursive File Search with rglob
File: 02_examples.py
"""
from pathlib import Path

def demonstrate_rglob() -> None:
    # Walk parent root repository directory searching for all .py files
    root_dir = Path(__file__).parent.parent.parent

    print(f"Searching for .py files in {root_dir.name}...")
    py_files = list(root_dir.rglob("*.py"))
    print(f"Total Python scripts discovered: {len(py_files)}")
    
    print("\nFirst 5 scripts:")
    for py_file in py_files[:5]:
        print(f"  - {py_file.relative_to(root_dir)}")


if __name__ == "__main__":
    demonstrate_rglob()
