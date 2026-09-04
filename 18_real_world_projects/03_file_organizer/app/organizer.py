"""
File Organizer Engine.
"""

from pathlib import Path


class FileOrganizer:
    @staticmethod
    def organize_directory(target_path: Path) -> dict[str, int]:
        counts: dict[str, int] = {}
        for item in target_path.iterdir():
            if item.is_file() and not item.name.startswith("."):
                ext = item.suffix.lstrip(".").lower() or "misc"
                dest_dir = target_path / ext
                dest_dir.mkdir(exist_ok=True)
                item.rename(dest_dir / item.name)
                counts[ext] = counts.get(ext, 0) + 1
        return counts
