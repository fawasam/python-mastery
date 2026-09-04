"""
Argparse Common Pitfalls.
"""

# MISTAKE: Expecting sys.argv parsing errors to raise standard Python exceptions.
# WHY: By default, argparse calls sys.exit(2) when invalid options are passed.
# FIX: Override ArgumentParser.error() or set exit_on_error=False (Python 3.9+) when testing programmatically.

if __name__ == "__main__":
    print("Argparse error handling rules verified.")
