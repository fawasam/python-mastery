# Building Production Command-Line Tools

## What You Will Learn
- Designing CLI user experience (UX) and exit codes (`0` for success, non-zero for errors)
- Reading standard input (`sys.stdin`) and writing to stdout/stderr
- Progress bars and interactive prompt confirmations
- Packaging CLI tools with `pyproject.toml` console scripts

## Why This Matters
Production-grade CLI tools behave predictably when piped together in Unix shell workflows (e.g. `cat file.txt | mytool --filter | jq .`). Respecting exit codes, stdout vs stderr separation, and signal handling ensures seamless integration.

## Core Concepts

### 1. Exit Codes
- `0`: Success
- `1`: General error
- `2`: Misuse of shell builtins / CLI parsing error

### 2. Standard Streams
- `sys.stdout`: Primary data output stream (pipeable to other tools).
- `sys.stderr`: Error and log messages (keeps stdout clean).

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and verify solutions in `05_solution.py`.

## Next Topic
Proceed to `../configuration/`.
