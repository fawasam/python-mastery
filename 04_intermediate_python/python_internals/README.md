# Python Internals & Execution Model

## What You Will Learn
* How Python source code is parsed, compiled to **Bytecode**, and executed by the CPython virtual machine.
* Disassembling Python code using the `dis` module.
* Inspecting function code objects (`func.__code__`).
* Understanding bytecode instructions (`LOAD_FAST`, `STORE_FAST`, `BINARY_OP`, `CALL`).
* How global/local lookup tables function internally.

## Why This Matters
Peeking under the hood at CPython bytecode demystifies why certain Python constructs run fast (e.g. local variable lookups via `LOAD_FAST`) while others incur dynamic overhead (global attribute resolution).

## Prerequisites
* Functions and Scope (`01_beginner/13_functions`, `01_beginner/14_scope`)

## Core Concepts

### CPython Execution Pipeline
1. **Source Code**: Python source files (`.py`).
2. **AST (Abstract Syntax Tree)**: Parsed structural tree.
3. **Bytecode**: Platform-independent intermediate instruction stream (`.pyc` files).
4. **CPython VM**: Evaluates bytecode loop using stack operations.

### Disassembling Code
```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

## Common Mistakes
* **Assuming bytecode is machine code**: Bytecode is run by the Python interpreter loop (`ceval.c`), not directly by CPU hardware.
* **Micro-optimizing based on instruction count alone**: A single bytecode instruction like `BUILD_LIST` might execute significantly faster in C than multiple lower-level instructions.

## Exercises
See `04_exercises.py` to practice analyzing function code objects and disassembling functions.
