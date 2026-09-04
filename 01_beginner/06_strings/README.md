# Topic 06: Strings, Indexing, Slicing & Methods

## What You Will Learn
- String immutability in Python.
- Indexing (0-based positive, negative indexing from the end `-1`).
- String slicing notation `[start:stop:step]`.
- Essential string methods: `.upper()`, `.lower()`, `.strip()`, `.replace()`, `.split()`, `.join()`, `.find()`, `.startswith()`, `.endswith()`.

## Why This Matters
Text processing, log parsing, data sanitization, API payload extraction, and natural language tasks rely heavily on Python's powerful string manipulation methods.

## Core Concepts
1. **Immutability**: Once created, strings cannot be modified in place. Operations returning "modified" strings create new string objects in memory.
2. **Slicing (`[start:stop:step]`)**:
   - `start`: inclusive index.
   - `stop`: exclusive index.
   - `step`: stride step (e.g. `::-1` reverses a string).
3. **Joining & Splitting**:
   - `.split(",")` splits string into a `list` of strings.
   - `",".join(list_of_strings)` joins a list into a single string.

## Syntax
```python
text = "Python Programming"

# Slicing
first_word = text[0:6]        # "Python"
reversed_text = text[::-1]    # "gnimmargorP nohtyP"

# Methods
clean_text = "   hello   ".strip().upper()  # "HELLO"
words = "apple,banana,cherry".split(",")   # ['apple', 'banana', 'cherry']
```

## Next Topic
Next: `07_conditionals` — Control flow using `if`, `elif`, `else`, nested conditions, and ternary expressions.
