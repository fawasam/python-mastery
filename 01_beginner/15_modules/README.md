# Topic 15: Modules, Imports & Standard Library

## What You Will Learn
- What a module is in Python (any `.py` file).
- Importing syntax variants:
  - `import math`
  - `from math import sqrt, pi`
  - `import datetime as dt` (aliasing)
- Understanding `sys.path` search order.
- Standard Library highlights: `math`, `random`, `sys`, `os`, `time`, `collections`.
- `if __name__ == "__main__":` idiom for script execution vs module import.

## Why This Matters
Modular design breaks code into manageable, reusable single-responsibility files. Proper import management prevents circular dependencies and namespace pollution.

## Core Concepts
1. **Module**: A single Python file containing functions, classes, and variables.
2. **`__name__` Variable**: When Python executes a script directly, `__name__` is `"__main__"`. When imported as a module, `__name__` is the module's file basename.
3. **`sys.path`**: A list of directory paths Python searches when locating modules to import.

## Syntax
```python
import math
from random import randint
import datetime as dt

radius = 5.0
area = math.pi * (radius ** 2)
random_id = randint(1000, 9999)
now = dt.datetime.now()
```

## Next Topic
Next: `16_exceptions` — Basic exception handling with `try`, `except`, `else`, and `finally`.
