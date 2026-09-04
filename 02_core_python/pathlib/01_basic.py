"""
Topic: Pathlib Basics & Division Operator Joining
File: 01_basic.py
"""
from pathlib import Path

def demonstrate_pathlib_basics() -> None:
    # 1. Building paths cleanly using / operator
    base_dir = Path(__file__).parent
    target_file = base_dir / "data" / "reports" / "summary.csv"

    print(f"Full Path:    {target_file}")
    print(f"Filename:     {target_file.name}")
    print(f"Stem (Name):  {target_file.stem}")
    print(f"Extension:   {target_file.suffix}")
    print(f"Parent Dir:   {target_file.parent.name}")

    # 2. Creating directory structure on disk
    report_dir = base_dir / "data" / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    print(f"\nDirectory created: {report_dir.exists()}")

    # Cleanup test created dirs
    if report_dir.exists():
        report_dir.rmdir()
        report_dir.parent.rmdir()


if __name__ == "__main__":
    demonstrate_pathlib_basics()
