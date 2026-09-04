# Python Bytecode and `dis` Module Internals

## What You Will Learn
- Understanding CPython Bytecode compilation (`.pyc` files and `__pycache__`)
- Disassembling Python functions into opcodes using standard library `dis`
- Code objects (`function.__code__`, `co_code`, `co_consts`, `co_varnames`)
- Stack-based virtual machine execution architecture (LOAD_FAST, BINARY_OP, RETURN_VALUE)

## Why This Matters
Python source code compiles into intermediate bytecode instructions before being interpreted by the CPython virtual machine. Inspecting bytecode reveals exact operation costs and execution optimization opportunities.

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and check `05_solution.py`.

## Next Topic
Proceed to `../ast/`.
