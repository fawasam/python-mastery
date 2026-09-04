# Topic 17: Basic File Handling & `pathlib`

## What You Will Learn
- Opening files using the built-in `open()` function.
- File modes: `"r"` (read), `"w"` (overwrite), `"a"` (append), `"b"` (binary).
- Using context managers (`with open(...) as file:`) for deterministic file handle closing.
- Reading techniques: `.read()`, `.readline()`, `.readlines()`, and line-by-line streaming iteration.
- Modern file path manipulation using Python 3's `pathlib.Path`.

## Why This Matters
File operations are central to loading configurations, parsing logs, writing reports, and processing raw datasets. Context managers (`with`) prevent file descriptor leaks that cause system instability.

## Core Concepts
1. **Context Manager (`with`)**: Guarantees that files are closed automatically upon exiting the code block, even if exceptions occur.
2. **`pathlib.Path`**: Object-oriented filesystem path manipulation replacing legacy `os.path`.
3. **File Modes**:
   - `"w"` creates or completely overwrites an existing file.
   - `"a"` creates or appends new content to the end of an existing file.

## Syntax
```python
from pathlib import Path

file_path = Path("logs/app.log")

# Writing text
with file_path.open("w", encoding="utf-8") as f:
    f.write("INFO: System initialized\n")

# Reading line-by-line
if file_path.exists():
    with file_path.open("r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
```

## Next Topic
Next: Section 1 Mini-Project — Building a complete personal finance & expense tracker CLI application!
