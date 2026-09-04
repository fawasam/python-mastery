# Python Language Interview Preparation Guide

## Overview
Comprehensive interview questions and detailed technical explanations covering Python internals, memory model, GIL, typing, data structures, and async runtime.

---

### Question 1: What is the Python Global Interpreter Lock (GIL) and why does it exist?

**Short Answer:**
The GIL is a mutex in CPython preventing multiple native threads from executing Python bytecodes simultaneously. It simplifies memory management and C extensions but restricts CPU-bound multithreading to a single core.

**Detailed Answer:**
CPython’s memory management uses reference counting. Without the GIL, concurrent operations in multiple OS threads could cause race conditions when incrementing/decrementing `ob_refcnt`. The GIL ensures thread-safety at the bytecode instruction level. For I/O-bound operations (e.g. network requests or file reads), CPython releases the GIL while waiting. For CPU-bound tasks, multiprocessing or C extensions (like NumPy) must be used to bypass the GIL.

**Code Example:**
```python
import threading
import time

count = 0

def increment():
    global count
    for _ in range(1_000_000):
        count += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

t1.start()
t2.start()
t1.join()
t2.join()

# GIL ensures bytecode execution safety, but race conditions can still occur on non-atomic ops
print(f"Final Count: {count}")
```

**Follow-up Question:**
How does Python 3.13 / 3.14 handle experimental free-threaded Python (no-GIL build)?

**Common Interview Trap:**
Confusing the GIL with general thread-safety. GIL prevents simultaneous bytecode execution, but high-level Python operations (`count += 1`) consist of multiple bytecodes (`LOAD_FAST`, `BINARY_OP`, `STORE_FAST`) and are NOT atomic!

---

### Question 2: What is the difference between `is` and `==` in Python?

**Short Answer:**
`==` checks for value equality (invoking `__eq__`), while `is` checks for object identity (memory address comparison `id(a) == id(b)`).

**Detailed Answer:**
In Python, every object has an identity, type, and value. `a == b` evaluates whether the contents/values represented by `a` and `b` are equal. `a is b` evaluates whether `a` and `b` refer to the exact same object in RAM (`id(a) == id(b)`).

**Code Example:**
```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True (equal values)
print(a is b)  # False (distinct objects in memory)
print(a is c)  # True (c references the same memory object as a)
```

**Follow-up Question:**
Why does `a = 256; b = 256; a is b` evaluate to `True`, but `a = 257; b = 257; a is b` evaluate to `False` in REPL?

**Common Interview Trap:**
Relying on integer caching / string interning optimizations. CPython caches small integers between `-5` and `256`. Testing `a is 256` might be `True`, but `a is 1000` is `False`. Never use `is` for value comparison!

---

### Question 3: What is a Python Generator and how does it differ from a List?

**Short Answer:**
A generator is a memory-efficient iterator evaluating elements lazily on-demand using `yield`, consuming $\mathcal{O}(1)$ space compared to $\mathcal{O}(n)$ for lists.

**Detailed Answer:**
When a function contains the `yield` keyword, calling it returns a generator object without executing the function body immediately. Each call to `next()` or iteration step resumes execution until the next `yield` statement, preserving stack frame state. This allows processing datasets larger than RAM capacity.

**Code Example:**
```python
import sys

# List comprehension: builds 1M integers in RAM
list_data = [x for x in range(1_000_000)]
print(f"List RAM Memory Size: {sys.getsizeof(list_data)} bytes")

# Generator expression: O(1) memory pointer
gen_data = (x for x in range(1_000_000))
print(f"Generator RAM Memory Size: {sys.getsizeof(gen_data)} bytes")
```

**Follow-up Question:**
What happens when a generator finishes yielding values?

**Common Interview Trap:**
Trying to iterate over a generator twice. Generators are single-pass iterators. Once exhausted, subsequent iterations yield zero items without raising errors in loops.

---

### Question 4: How does Python's Method Resolution Order (MRO) work in multiple inheritance?

**Short Answer:**
Python uses the C3 Linearization algorithm to determine the order in which base classes are searched when calling inherited methods or `super()`.

**Detailed Answer:**
C3 Linearization guarantees three properties: monotonicity (subclasses respect parent order), local precedence order, and consistency across inheritance hierarchies. You can inspect any class's MRO using `Class.mro()` or `Class.__mro__`.

**Code Example:**
```python
class A:
    def process(self):
        print("A")

class B(A):
    def process(self):
        print("B")
        super().process()

class C(A):
    def process(self):
        print("C")
        super().process()

class D(B, C):
    def process(self):
        print("D")
        super().process()

print("MRO for Class D:", [cls.__name__ for cls in D.mro()])
d = D()
d.process()  # Output order: D -> B -> C -> A
```

**Follow-up Question:**
What happens if you construct an invalid cyclic inheritance structure that violates C3 Linearization?

**Common Interview Trap:**
Assuming `super()` calls the immediate parent class written in class definition. `super()` follows the MRO of the *starting instance*, so calling `super()` inside `B` might invoke `C`!
