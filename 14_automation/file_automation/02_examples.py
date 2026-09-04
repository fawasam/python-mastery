"""
Advanced File Automation: SHA256 Duplicate File Finder.
"""

hashlib = __import__("hashlib")
from pathlib import Path
import tempfile


def compute_file_hash(file_path: Path) -> str:
    """Compute SHA256 hash of a file reading in 64KB chunks."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def find_duplicate_files(target_dir: Path) -> dict[str, list[Path]]:
    """Scan directory for duplicate files matching by SHA256 content hash."""
    seen_hashes: dict[str, list[Path]] = {}
    
    for path in target_dir.rglob("*"):
        if path.is_file():
            file_hash = compute_file_hash(path)
            seen_hashes.setdefault(file_hash, []).append(path)
            
    return {h: paths for h, paths in seen_hashes.items() if len(paths) > 1}


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        (tmp_path / "original.txt").write_text("Identical content body")
        (tmp_path / "copy.txt").write_text("Identical content body")
        (tmp_path / "unique.txt").write_text("Unique content body")
        
        duplicates = find_duplicate_files(tmp_path)
        print(f"Found {len(duplicates)} duplicate content group(s).")
