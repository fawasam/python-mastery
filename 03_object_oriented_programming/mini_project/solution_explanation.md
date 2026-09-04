# Mini-Project 03 — Solution Explanation

## Architecture Overview
The Object-Oriented Library Management System combines core OOP principles:

1. **Encapsulation & Properties**:
   - `Book` exposes a read-only property `@property def is_borrowed()` while managing internal `_is_borrowed` boolean state securely.
   - `Member` manages private set `_borrowed_isbns` internally to prevent external mutation without validation.

2. **Dataclasses**:
   - `Transaction` uses `@dataclass` for concise, clean recording of audit transactions with default UTC timestamp formatting.

3. **Composition & Service Layer**:
   - `Library` HAS-A dictionary catalog of `Book` items and HAS-A registry of `Member` items.
   - Orchestrates transactions while handling domain constraints (book availability, member limits).

## Run Verification
Execute the OOP library main script:
```bash
python 03_object_oriented_programming/mini_project/main.py
```
