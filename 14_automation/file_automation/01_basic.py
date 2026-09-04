"""
File Automation Basics: Organizing Files by Extension.
"""

from pathlib import Path
import tempfile


def organize_directory_by_extension(target_dir: Path) -> dict[str, int]:
    """
    Scan target_dir and sort files into extension subfolders (e.g. 'txt', 'pdf', 'jpg').
    
    Returns counts of organized files by extension.
    """
    counts: dict[str, int] = {}
    
    for item in target_dir.iterdir():
        if item.is_file() and not item.name.startswith("."):
            ext = item.suffix.lstrip(".").lower() or "no_extension"
            dest_folder = target_dir / ext
            dest_folder.mkdir(exist_ok=True)
            
            # Move file into destination folder
            item.rename(dest_folder / item.name)
            counts[ext] = counts.get(ext, 0) + 1
            
    return counts


if __name__ == "__main__":
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        
        # Create dummy test files
        (tmp_path / "report.pdf").write_text("PDF content")
        (tmp_path / "notes.txt").write_text("Text notes")
        (tmp_path / "summary.txt").write_text("Summary text")
        
        print("Organizing temporary directory...")
        results = organize_directory_by_extension(tmp_path)
        print("Organization Results:", results)
