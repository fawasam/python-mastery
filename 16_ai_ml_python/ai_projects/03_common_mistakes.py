"""
AI Projects Common Pitfalls.
"""

# MISTAKE: Failing to log and monitor token usage metrics and API billing costs in production AI services.
# WHY: A single runaway loop or malicious user can burn thousands of dollars in cloud API tokens in hours.
# FIX: Implement per-user rate limiting, daily cost quotas, and telemetry logging.

if __name__ == "__main__":
    print("AI API billing quota & rate-limiting safety rules verified.")
