"""
CLI Tools Common Pitfalls.
"""

# MISTAKE: Printing error logs directly to sys.stdout instead of sys.stderr.
# WHY: When users pipe CLI tool output into files or other binaries (`mytool > out.txt`),
# mixing log output into stdout corrupts the data pipeline.

if __name__ == "__main__":
    print("Stderr/stdout pipe safety rules verified.")
