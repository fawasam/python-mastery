# Garbage Collection in Python

## What You Will Learn
* The Python `gc` module interface.
* Generational Garbage Collection (Generations 0, 1, and 2).
* How Python detects and collects reference cycles.
* Disabling, enabling, and manually triggering garbage collection (`gc.collect()`).
* Tuning GC thresholds (`gc.set_threshold()`).

## Why This Matters
While reference counting handles ~90% of object deallocations immediately, cyclic references (where objects reference each other directly or indirectly) require Python's generational collector. Understanding GC behavior helps diagnose latency spikes in high-throughput applications.

## Prerequisites
* Memory Management (`04_intermediate_python/memory_management`)

## Core Concepts

### Generational Garbage Collection
Python categorizes container objects (lists, dicts, custom objects) into three generations:
- **Generation 0**: Newly allocated objects. Collected most frequently.
- **Generation 1**: Objects surviving Generation 0 collections.
- **Generation 2**: Long-lived objects surviving Generation 1 collections. Collected least frequently.

### The `gc` Module
- `gc.collect()`: Runs a full collection pass immediately.
- `gc.get_stats()`: Inspects collection counts and stats per generation.
- `gc.disable()` / `gc.enable()`: Temporarily suspends or restores automatic GC (e.g. during batch import loops).

## Syntax
```python
import gc

# Disable GC for a performance-critical loop
gc.disable()
try:
    # Run heavy operations
    pass
finally:
    gc.enable()
    gc.collect()  # Clean up orphaned cyclic objects
```

## Common Mistakes
* **Disabling GC permanently**: Can lead to memory leakage if your code or 3rd-party libraries construct circular reference graphs.
* **Over-calling `gc.collect()`**: Explicitly triggering full GC passes inside tight loops degrades performance.

## Exercises
See `04_exercises.py` to practice inspecting cycle collections and benchmarking GC impact.
