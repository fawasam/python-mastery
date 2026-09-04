# Topic: Modern File System Operations with `pathlib`

## What You Will Learn
- `pathlib.Path` objects vs string paths.
- Path resolution & joining: `/` operator (`base_dir / "subdir" / "file.txt"`).
- Inspecting properties: `.name`, `.stem`, `.suffix`, `.parent`, `.parts`, `.exists()`, `.is_file()`, `.is_dir()`.
- Directory manipulation: `.mkdir(parents=True, exist_ok=True)`, `.rmdir()`, `.unlink()`.
- Recursive search with `.glob()` and `.rglob()`.

## Core Concepts
1. **Object-Oriented Paths**: `pathlib` replaces legacy string concatenation and `os.path.join()` with cross-platform `Path` objects and the `/` operator.
2. **`exist_ok=True`**: Prevents `FileExistsError` when creating directories.

## Syntax
```python
from pathlib import Path

path = Path("logs/2026/app.log")
print(path.stem)    # "app"
print(path.suffix)  # ".log"
print(path.parent)  # PosixPath("logs/2026")
```

## Next Topic
Next: `os_sys` — System calls, process environment variables (`os.environ`), command-line args (`sys.argv`), and process exit codes (`sys.exit`).
