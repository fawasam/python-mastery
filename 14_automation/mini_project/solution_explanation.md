# Automation Mini Project Architectural Breakdown

## Features Demonstrated
1. **Pathlib File Traversal**: Uses `glob("*.log")` to discover target log files dynamically.
2. **ZipFile Compression**: Utilizes `ZIP_DEFLATED` compression to save disk space.
3. **Safe File Removal**: Deletes original `.log` files only after verifying successful archive write.
4. **Disk Auditing**: Uses `shutil.disk_usage()` for telemetry monitoring.
