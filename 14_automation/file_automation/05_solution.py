"""
Solutions: File Automation Exercises.
"""

from pathlib import Path
import tempfile


def count_files_by_extension(target_dir: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    for p in target_dir.rglob("*"):
        if p.is_file():
            ext = p.suffix.lower() or ".no_ext"
            counts[ext] = counts.get(ext, 0) + 1
    return counts


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp_dir:
        p = Path(tmp_dir)
        (p / "a.py").touch()
        (p / "b.py").touch()
        (p / "c.txt").touch()
        print("Extension counts:", count_files_by_extension(p))
