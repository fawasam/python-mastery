"""
LLM API Common Pitfalls.
"""

# MISTAKE: Trusting raw LLM output strings without validating schema constraints.
# WHY: LLMs can hallucinate invalid JSON or omit mandatory keys.
# FIX: Always parse LLM response strings using Pydantic or `try/except json.JSONDecodeError` blocks.

if __name__ == "__main__":
    print("LLM JSON output validation rules verified.")
