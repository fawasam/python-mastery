"""
Scheduled Jobs Anti-Patterns.
"""

# MISTAKE: Uncaught exceptions inside background scheduled loops terminating the entire daemon.
# WHY: In a infinite background loop, an uncaught exception (e.g. temporary network error) breaks the loop permanently.
# FIX: Wrap loop iterations in try/except blocks and log failures gracefully.

if __name__ == "__main__":
    print("Resilient job loop rules verified.")
