# Command-Line Interfaces with `argparse`

## What You Will Learn
- Building standard command-line interfaces using Python's built-in `argparse` module
- Positional vs optional arguments
- Flag options, default values, and parameter types (`int`, `str`, `Path`)
- Subcommands (e.g. `git commit` vs `git push`)

## Why This Matters
`argparse` is part of Python's standard library. Understanding `argparse` lets you build robust CLI tools without requiring third-party dependencies.

## Core Concepts

### Argument Types
- **Positional Arguments**: Required arguments specified by position on the command line.
- **Optional Arguments / Flags**: Prefixed with `-` or `--` (e.g., `--verbose`, `-v`).
- **Subcommands**: `add_subparsers()` lets a single script handle sub-commands with dedicated options.

## Examples
See `01_basic.py` (Basic parser) and `02_examples.py` (Subcommands parser).

## Exercises
Complete exercises in `04_exercises.py` and verify in `05_solution.py`.

## Next Topic
Proceed to `../typer/`.
