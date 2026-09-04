"""
AI Projects Basics: Building Input Guardrails (PII & Injection Sanitizer).
"""

import re


class SafetyGuardrail:
    """Sanitizes incoming prompts to protect against prompt injection and PII leakage."""
    @staticmethod
    def sanitize_prompt(prompt: str) -> str:
        # 1. Check for basic prompt injection keywords
        forbidden_patterns = [r"ignore previous instructions", r"system prompt override"]
        for pattern in forbidden_patterns:
            if re.search(pattern, prompt, re.IGNORECASE):
                raise ValueError("Prompt injection attack detected.")

        # 2. Scrub SSN / Credit Card PII numbers
        scrubbed = re.sub(r"\b\d{3}-\d{2}-\d{4}\b", "[REDACTED_SSN]", prompt)
        return scrubbed


if __name__ == "__main__":
    raw_prompt = "Hello, please review employee account with SSN 123-45-6789."
    clean_prompt = SafetyGuardrail.sanitize_prompt(raw_prompt)
    print("Sanitized Prompt:", clean_prompt)
