"""
Topic: Pathlib Solutions
File: 05_solution.py
"""
from pathlib import Path

def level_1_easy() -> None:
    p = Path("temp") / "cache" / "data.bin"
    print(f"Stem: '{p.stem}' | Suffix: '{p.suffix}'")


def level_2_medium() -> None:
    nested = Path("build") / "artifacts" / "logs"
    nested.mkdir(parents=True, exist_ok=True)
    print(f"Created nested directory: {nested.exists()}")
    # Cleanup
    if nested.exists():
        nested.rmdir()
        nested.parent.rmdir()
        nested.parent.parent.rmdir()


def level_3_hard() -> int:
    current_dir = Path(__file__).parent
    total_bytes = sum(f.stat().st_size for f in current_dir.glob("*.py"))
    print(f"Total bytes of .py files in topic dir: {total_bytes:,} bytes")
    return total_bytes


def level_4_real_world(target_dir: Path) -> None:
    if not target_dir.exists():
        return
    text_dir = target_dir / "texts"
    img_dir = target_dir / "images"

    for file in target_dir.glob("*.*"):
        if file.suffix == ".txt":
            text_dir.mkdir(exist_ok=True)
            file.rename(text_dir / file.name)
            print(f"Moved {file.name} -> texts/")
        elif file.suffix == ".png":
            img_dir.mkdir(exist_ok=True)
            file.rename(img_dir / file.name)
            print(f"Moved {file.name} -> images/")


if __name__ == "__main__":
    print("--- Level 1 ---")
    level_1_easy()

    print("\n--- Level 2 ---")
    level_2_medium()

    print("\n--- Level 3 ---")
    level_3_hard()
