# Memory Management in Python

## What You Will Learn
* How Python manages memory internally (Objects, References, PyObject, Heaps).
* Object reference counts and `sys.getrefcount()`.
* Object identity vs Equality (`is` vs `==`).
* Small integer caching and string interning optimizations.
* Using `weakref` to prevent memory leaks and circular dependencies.

## Why This Matters
While Python features automatic memory management, understanding object lifecycle, reference counting, and weak references is crucial for preventing memory leaks in high-performance services, desktop applications, and long-running daemons.

## Prerequisites
* Classes & Objects (`03_object_oriented_programming/classes_objects`)

## Core Concepts

### 1. Reference Counting
Every Python object (`PyObject`) contains a reference count header (`ob_refcnt`). When an object is assigned to a variable, passed to a function, or added to a list, its reference count increments. When references go out of scope or are deleted with `del`, the reference count decrements. When it hits `0`, memory is deallocated immediately.

### 2. Weak References (`weakref`)
A `weakref.ref` or `weakref.WeakValueDictionary` allows referencing an object WITHOUT incrementing its reference count. This is ideal for caching mechanisms and parent-child hierarchy linkages.

## Syntax
```python
import sys
import weakref

x = [1, 2, 3]
print(sys.getrefcount(x))  # Note: getrefcount adds 1 temporary reference

w = weakref.ref(x)
print(w())  # Access object [1, 2, 3]
del x
print(w())  # None (object was deallocated!)
```

## Common Mistakes
* **Assuming `del obj` frees memory directly**: `del` only deletes the name binding and decrements the reference count. If other references exist, the object stays alive in memory.
* **Creating strong circular references**: If object A points to B and B points to A, their reference counts never reach 0 through normal scope exiting.

## Exercises
See `04_exercises.py` to practice creating weak reference caches and inspecting object reference graphs.
