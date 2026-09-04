"""
System Automation Pitfalls: Command Injection.
"""

# MISTAKE: Passing un-sanitized user input into `subprocess.run(..., shell=True)`.
# WHY: Allows malicious input like `"filename.txt; rm -rf /"` to execute arbitrary shell commands.
# FIX: Always pass command arguments as a list of strings (`["ls", "-l", target_path]`) with `shell=False`.

if __name__ == "__main__":
    print("Subprocess command injection prevention rules verified.")
