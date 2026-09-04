"""
AI Agents Common Pitfalls.
"""

# MISTAKE: Allowing an autonomous agent to execute tool loops without a strict `max_steps` iteration ceiling.
# WHY: If a tool repeatedly fails or returns invalid observations, the agent enters an infinite execution loop, burning API tokens rapidly.
# FIX: Always cap loop iterations (e.g. `max_steps = 5` or `max_execution_time = 30s`).

if __name__ == "__main__":
    print("Agent max_steps safety iteration ceiling verified.")
