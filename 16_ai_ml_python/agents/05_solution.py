"""
Solutions: AI Agent Exercises.
"""

from typing import Callable


def dispatch_tool_call(tools: dict[str, Callable[[str], str]], name: str, arg: str) -> str:
    if name not in tools:
        return f"Error: Tool '{name}' not found"
    return tools[name](arg)


if __name__ == "__main__":
    registry = {"echo": lambda x: f"Echo: {x}"}
    print(dispatch_tool_call(registry, "echo", "hello"))
