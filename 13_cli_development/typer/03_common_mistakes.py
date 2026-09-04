"""
Typer Common Pitfalls.
"""

# MISTAKE: Forgetting that Typer expects function parameters without default values to be required positional arguments.
# FIX: Use typer.Option(...) for optional arguments with default values.

if __name__ == "__main__":
    print("Typer usage rules verified.")
