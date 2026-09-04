# Topic: CSV Parsing & Writing (`csv.DictReader` / `csv.DictWriter`)

## What You Will Learn
- Reading CSV lines using `csv.reader` vs `csv.DictReader`.
- Writing CSV lines using `csv.writer` vs `csv.DictWriter`.
- Setting custom delimiters (e.g. tabs `\t` or semicolons `;`).
- Handling header rows and quotes (`newline=""` rule).

## Core Concepts
1. **`csv.DictReader`**: Parses CSV rows into Python dictionaries using header keys.
2. **`csv.DictWriter`**: Writes dictionary records into CSV rows using a specified `fieldnames` list.
3. **`newline=""` Requirement**: When opening CSV files in Python on Windows/Unix, `newline=""` prevents extra blank lines from being written.

## Next Topic
Next: `pathlib` — Object-oriented path manipulation and filesystem operations.
