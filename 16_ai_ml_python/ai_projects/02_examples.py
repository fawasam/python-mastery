"""
Advanced AI Projects: Telemetry Logging and Token Metering.
"""

from dataclasses import dataclass, field
import time


@dataclass
class LLMTelemetry:
    """Tracks token consumption, latency, and operational cost of AI requests."""
    prompt_tokens: int
    completion_tokens: int
    latency_seconds: float
    estimated_cost_usd: float = field(init=False)

    def __post_init__(self) -> None:
        # Estimated cost calculation ($0.0015 / 1K input, $0.002 / 1K output)
        cost_input = (self.prompt_tokens / 1000.0) * 0.0015
        cost_output = (self.completion_tokens / 1000.0) * 0.0020
        self.estimated_cost_usd = round(cost_input + cost_output, 6)


if __name__ == "__main__":
    start = time.perf_counter()
    time.sleep(0.02)  # Simulate API latency
    duration = time.perf_counter() - start

    telemetry = LLMTelemetry(prompt_tokens=450, completion_tokens=120, latency_seconds=duration)
    print("AI Call Telemetry Summary:", telemetry)
