"""
Advanced C-API Concepts: C Structures and Memory Layouts in Python.
"""

import ctypes


class CPoint(ctypes.Structure):
    """Mapping C struct { int x; int y; } using ctypes.Structure."""
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_int)
    ]


if __name__ == "__main__":
    point = CPoint(x=10, y=20)
    print(f"C Struct Memory Layout (Point x={point.x}, y={point.y})")
    print("Struct size in bytes:", ctypes.sizeof(point))
