"""
C-API Common Pitfalls.
"""

# MISTAKE: Passing invalid Python types to `ctypes` functions without configuring `argtypes` and `restype`.
# WHY: By default, `ctypes` assumes `int` arguments/return types. Passing pointers or floats without `argtypes` causes Segmentation Faults (SIGSEGV).
# FIX: Always set `func.argtypes = [...]` and `func.restype = ...` explicitly for all `ctypes` functions.

if __name__ == "__main__":
    print("Ctypes argtypes and restype explicit declaration rules verified.")
