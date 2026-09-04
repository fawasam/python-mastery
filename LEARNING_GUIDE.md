# Python Mastery — Learning Guide

Welcome to **Python Mastery**! This repository is designed to be your complete, interactive curriculum for mastering Python software engineering from ground zero to production quality.

---

## 🎯 Recommended Learning Workflow

To get the maximum value out of this repository, follow this systematic approach for **every topic**:

```text
1. Read Topic README
      ↓
2. Study basic code (01_basic.py)
      ↓
3. Run the code & observe outputs
      ↓
4. Explore real-world examples (02_examples.py)
      ↓
5. Review common mistakes (03_common_mistakes.py)
      ↓
6. Solve exercises yourself (04_exercises.py)
      ↓
7. Compare with official solutions (05_solution.py)
      ↓
8. Complete Section Mini-Project
      ↓
9. Mark completion in PROGRESS.md
```

---

## 💡 Mindset & Study Principles

### 1. Don't Just Copy-Paste — Type It Out
Muscle memory matters. Typing out code forces you to pay attention to syntax, indentation, and structure.

### 2. Run Every Script
Do not just read Python code like a book. Run it in your shell using your virtual environment:

```bash
source .venv/bin/activate
python 01_beginner/01_hello_world/01_basic.py
```

### 3. Embrace Errors & Debugging
When Python raises an exception:
- Read the traceback **from the bottom up**.
- Identify the file name, line number, and error message.
- Ask: *"Why did the runtime reach this state?"*

### 4. Solve Exercises BEFORE Looking at Solutions
`04_exercises.py` contains incomplete function stubs with `raise NotImplementedError(...)`. Work on completing them without looking at `05_solution.py`. Only open `05_solution.py` after attempting all 4 levels!

---

## 🛠 Required Tools & Setup

1. **Python 3.12+**: Ensure `python3 --version` returns 3.12 or higher.
2. **Virtual Environment**:
   ```bash
   cd python-mastery
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Linter & Formatter**:
   - Run `ruff check .` to check for PEP 8 compliance.
   - Run `mypy .` for static type verification.
   - Run `pytest` to execute test suites.
