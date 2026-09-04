# Topic 01: Hello World & Python Fundamentals

## What You Will Learn
- How Python code is executed line-by-line by the Python interpreter.
- Using the `print()` function to output text to the terminal.
- How single-line and multi-line comments work in Python.
- Understanding Python's syntax simplicity compared to compiled languages like C++ or Java.

## Why This Matters
"Hello, World!" is the universal entry point to any programming language. It verifies that your environment, Python interpreter, and script execution setup are functioning correctly.

## Prerequisites
- Python 3.12+ installed.
- Access to a terminal or IDE terminal window.

## Core Concepts
1. **Interpreter**: Python code is interpreted line-by-line from top to bottom.
2. **Built-in Functions**: `print()` is a pre-packaged function in Python that sends output to standard output (the screen).
3. **Comments**: Text ignored by the interpreter, used exclusively for developer documentation and notes (`#` or triple quotes `"""..."""`).

## Syntax
```python
# This is a single-line comment
print("Hello, World!")  # Output a string to stdout
```

## Examples
```python
print("Welcome to Python Mastery!")
print("Python was created by Guido van Rossum in 1991.")
```

## Common Mistakes
- **Capitalization Error**: Writing `Print("Hello")` instead of `print("Hello")`. Python is case-sensitive!
- **Missing Quotes**: Writing `print(Hello)` without quotation marks. Python will treat `Hello` as an undefined variable.

## Best Practices
- Use clean, clear strings for console output.
- Write meaningful comments that explain *why* code exists rather than stating obvious operations.

## Exercises
- Easy: Print your name and favorite programming language.
- Medium: Print a multi-line message using newline characters `\n` or triple quotes.
- Hard: Combine multiple items inside a single `print()` statement.
- Real World: Create a welcome banner for a command-line application.

## Interview Questions
- **Q**: Is Python compiled or interpreted?
  - **A**: Python is an interpreted language. Python source code (`.py`) is compiled into bytecode (`.pyc`), which is then executed by the Python Virtual Machine (PVM).

## Real-World Usage
Command-line interface (CLI) banners, logging, user prompts, and diagnostic outputs all rely on standard output.

## Next Topic
Next: `02_variables` — Learn how to store and manage data in memory.
