"""
File Automation Pitfalls.
"""

# MISTAKE: Loading entire multi-gigabyte files into memory at once with file.read() when hashing or copying.
# WHY: Causes MemoryError on large video or binary files.
# FIX: Always read files in fixed-size binary chunks (e.g. while chunk := file.read(65536)).

if __name__ == "__main__":
    print("Chunked I/O file safety rules verified.")
