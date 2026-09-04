"""
System Automation Basics: Subprocess execution and output capture.
"""

import subprocess


def run_system_command(command: list[str]) -> tuple[int, str, str]:
    """
    Execute a system command safely without shell=True to avoid command injection vulnerabilities.
    
    Returns (return_code, stdout, stderr).
    """
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        check=False
    )
    return result.returncode, result.stdout, result.stderr


if __name__ == "__main__":
    # Test running 'python3 --version' or 'python --version'
    code, stdout, stderr = run_system_command(["python3", "--version"])
    print(f"Command Exit Code: {code}")
    print(f"Stdout: {stdout.strip()}")
