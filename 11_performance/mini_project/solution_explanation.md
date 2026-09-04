# Mini Project Architectural Explanation: Performance Optimization

## Bottleneck Analysis & Fixes

### 1. List Search to Hash Set Conversion
- **Problem**: `rec.user_id in target_users` searched a list of 500 items for every record ($O(n \times m)$ complexity).
- **Fix**: Converted `target_users` to a `set` ($O(1)$ lookup complexity).
- **Impact**: Dramatic reduction in loop execution time.

### 2. Class Memory Overhead with `__slots__`
- **Problem**: Python default class instances store attributes in a dynamic `__dict__` dictionary, consuming ~300 bytes per instance.
- **Fix**: Used `__slots__` tuple declaration.
- **Impact**: Reduces object memory footprint by ~60-70% and speeds up attribute access.

### 3. LRU Caching for Repeated Computations
- **Problem**: Re-building formatted string keys dynamically on every loop iteration.
- **Fix**: Wrapped key construction in `@lru_cache(maxsize=128)`.
- **Impact**: Zero redundant string operations for identical endpoints.
