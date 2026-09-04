"""
Tests for File Organizer.
"""

from pathlib import Path
import tempfile
from app.organizer import FileOrganizer


def test_file_organizer() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp)
        (p / "file1.pdf").touch()
        (p / "file2.pdf").touch()
        
        counts = FileOrganizer.organize_directory(p)
        assert counts == {"pdf": 2}
        assert (p / "pdf" / "file1.pdf").exists()
