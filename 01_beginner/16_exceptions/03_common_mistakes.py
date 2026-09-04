"""
Topic: Common Exception Handling Mistakes
File: 03_common_mistakes.py
"""

def mistake_1_bare_except_clause() -> None:
    # ❌ WRONG: Bare `except:` catches KeyboardInterrupt, SystemExit, and hides bugs!
    # try:
    #     val = 10 / 0
    # except:
    #     pass

    # ✅ CORRECT: Catch specific exceptions or `except Exception:`
    try:
        val = 10 / 0
    except ZeroDivisionError as e:
        print(f"Specifically caught: {type(e).__name__}")


def mistake_2_swallowing_exceptions_silently() -> None:
    # ❌ WRONG: Catching exception and doing nothing (pass) makes debugging impossible!
    # try:
    #     res = int("bad")
    # except ValueError:
    #     pass

    # ✅ CORRECT: Log error or re-raise
    try:
        res = int("bad")
    except ValueError as e:
        print(f"Logged exception for diagnostic tracing: {e}")


if __name__ == "__main__":
    mistake_1_bare_except_clause()
    mistake_2_swallowing_exceptions_silently()
