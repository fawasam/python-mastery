# Building Modern CLI Applications with `typer`

## What You Will Learn
- Building CLI applications with `typer` using Python type hints
- Automatic CLI help text and option parsing
- Subcommands with `typer.Typer()` app groups
- Rich terminal output formatting (`typer.echo` / `rich`)

## Why This Matters
`typer` (built on Click) is the modern standard for Python CLI development. It eliminates boilerplate by leveraging Python 3.12 type annotations (`str`, `int`, `Annotated`, `Option`, `Argument`) to generate beautiful CLI tools automatically.

## Core Concepts

### 1. Simple Commands
Functions decorated with `@app.command()` become CLI subcommands.

### 2. Type Hint Integration
- Function parameters without defaults become positional arguments.
- Parameters with defaults (`= typer.Option(...)`) become flags.

```python
import typer

app = typer.Typer()

@app.command()
def hello(name: str, formal: bool = False):
    if formal:
        print(f"Good day, {name}.")
    else:
        print(f"Hello {name}!")
```

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and verify in `05_solution.py`.

## Next Topic
Proceed to `../command_line_tools/`.
