"""
Refactoring Anti-Patterns: Refactoring Without Test Safety Nets.
"""

# MISTAKE: Attempting large, sweeping refactors without having existing unit test coverage.
# WHY: Without tests, it is almost impossible to ensure that existing system behaviors were not broken during refactoring.
# RULE: Write unit tests FIRST to characterize current behavior, THEN refactor, THEN verify tests pass.

if __name__ == "__main__":
    print("Refactoring safety rules analyzed.")
