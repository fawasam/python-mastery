"""
Automation Mini Project: Automated Log Archiver and Disk Audit System.
"""

from datetime import datetime
from pathlib import Path
import shutil
import tempfile
import zipfile


def create_sample_logs(log_dir: Path) -> list[Path]:
    """Create sample log files for archiving demonstration."""
    files = []
    for name in ["app_access.log", "error_audit.log", "db_slow.log"]:
        file_path = log_dir / name
        file_path.write_text(f"Log entry timestamp: {datetime.now().isoformat()}\nSample log data body.")
        files.append(file_path)
    return files


def archive_logs(log_dir: Path, output_zip: Path) -> int:
    """Scan log_dir for .log files, package them into output_zip, and delete raw logs."""
    log_files = list(log_dir.glob("*.log"))
    if not log_files:
        return 0

    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as archive:
        for log_file in log_files:
            archive.write(log_file, arcname=log_file.name)
            log_file.unlink()  # Remove uncompressed file after archiving

    return len(log_files)


def main() -> None:
    print("=== Automated Log Archiver & Disk Audit System ===")
    
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        logs_folder = tmp_path / "logs"
        logs_folder.mkdir()
        
        # 1. Inspect initial disk metrics
        usage_before = shutil.disk_usage(tmp_dir)
        print(f"Disk space free before run: {usage_before.free / (1024**2):.2f} MB")

        # 2. Populate synthetic logs
        created_files = create_sample_logs(logs_folder)
        print(f"Created {len(created_files)} active log file(s).")

        # 3. Archive logs to Zip
        zip_destination = tmp_path / f"log_archive_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
        archived_count = archive_logs(logs_folder, zip_destination)
        
        print(f"Successfully compressed and archived {archived_count} log file(s).")
        print(f"Archive file created: {zip_destination.name} (Size: {zip_destination.stat().st_size} bytes)")
        
        # Verify raw log cleanup
        remaining_logs = list(logs_folder.glob("*.log"))
        print(f"Uncompressed log files remaining in folder: {len(remaining_logs)}")


if __name__ == "__main__":
    main()
