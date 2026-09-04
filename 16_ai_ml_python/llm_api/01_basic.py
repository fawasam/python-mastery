"""
LLM API Integration Basics: Structuring Prompt Messages and Mock Clients.
"""

from dataclasses import dataclass
from typing import Literal, Protocol


@dataclass
class ChatMessage:
    role: Literal["system", "user", "assistant"]
    content: str


class LLMClientProtocol(Protocol):
    def generate_completion(self, messages: list[ChatMessage], temperature: float = 0.7) -> str:
        ...


class MockLLMClient:
    """Mock LLM client returning simulated response payload for offline environments."""
    def generate_completion(self, messages: list[ChatMessage], temperature: float = 0.7) -> str:
        user_msg = messages[-1].content if messages else ""
        return f"[Simulated LLM Response to: '{user_msg}' (temp={temperature})]"


if __name__ == "__main__":
    messages = [
        ChatMessage(role="system", content="You are a helpful Python assistant."),
        ChatMessage(role="user", content="Explain Python dataclasses in one sentence.")
    ]
    
    client: LLMClientProtocol = MockLLMClient()
    response = client.generate_completion(messages, temperature=0.2)
    print("LLM Response:\n", response)
