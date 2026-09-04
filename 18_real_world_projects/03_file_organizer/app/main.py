"""
File Organizer CLI Main.
"""

from pathlib import Path
import tempfile
from app.organizer import FileOrganizer


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp)
        (p / "data.csv").write_text("1,2,3")
        (p / "notes.txt").write_text("hello")
        
        results = FileOrganizer.organize_directory(p)
        print("Organized Files:", results)


if __name__ == "__main__":
    main()
