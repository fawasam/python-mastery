"""
Python C-API Concepts: Interfacing C Standard Library via ctypes.
"""

import ctypes
import platform


def demonstrate_ctypes_standard_library() -> None:
    """Invoke C standard library functions (abs, strlen) via ctypes FFI bindings."""
    # Load system C standard library (libc)
    system = platform.system()
    if system == "Darwin":
        libc = ctypes.CDLL("libc.dylib")
    elif system == "Windows":
        libc = ctypes.cdll.msvcrt
    else:
        libc = ctypes.CDLL("libc.so.6")

    # Define C function signature for 'abs'
    libc.abs.argtypes = [ctypes.c_int]
    libc.abs.restype = ctypes.c_int

    # Invoke native C function
    result = libc.abs(-42)
    print(f"C libc.abs(-42) output via ctypes FFI: {result}")


if __name__ == "__main__":
    demonstrate_ctypes_standard_library()
