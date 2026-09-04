"""
Advanced LLM API: Structured JSON Output Extraction.
"""

import json
from dataclasses import dataclass


@dataclass
class SentimentAnalysisResult:
    sentiment: str  # "POSITIVE", "NEGATIVE", "NEUTRAL"
    confidence_score: float
    key_phrases: list[str]


def parse_structured_llm_json(raw_response: str) -> SentimentAnalysisResult:
    """Parse JSON string output returned by LLM into strongly-typed dataclass."""
    data = json.loads(raw_response)
    return SentimentAnalysisResult(
        sentiment=data.get("sentiment", "NEUTRAL"),
        confidence_score=float(data.get("confidence_score", 0.0)),
        key_phrases=data.get("key_phrases", [])
    )


if __name__ == "__main__":
    simulated_json_output = """
    {
        "sentiment": "POSITIVE",
        "confidence_score": 0.98,
        "key_phrases": ["fast performance", "excellent documentation"]
    }
    """
    result = parse_structured_llm_json(simulated_json_output)
    print("Parsed LLM Structured Result:", result)
