# Python C-API Concepts and Foreign Function Interfaces (FFI)

## What You Will Learn
- Interfacing C code with Python using standard library `ctypes`
- C-types bindings (`ctypes.c_int`, `ctypes.c_double`, `ctypes.c_char_p`)
- Calling external system C dynamic libraries (`.so` / `.dylib` / `.dll`)
- Reference counting (`Py_INCREF`, `Py_DECREF`) and GIL interaction in C extensions

## Why This Matters
Performance-critical libraries (NumPy, SciPy, PyTorch) call underlying C/C++ or Rust shared objects to bypass Python's interpreter overhead. Understanding `ctypes` allows binding native C libraries into Python without writing full C extensions.

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and check `05_solution.py`.

## Next Topic
Complete the Advanced Python Mini Project in `../mini_project/`.
