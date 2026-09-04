"""
Exercises: AI Agent Tool Dispatching.
"""

from typing import Callable


def dispatch_tool_call(tools: dict[str, Callable[[str], str]], name: str, arg: str) -> str:
    """
    Exercise: Dispatch call to tool function in tools dictionary.
    Return error string if tool name not found.
    
    Level 1 - Easy
    """
    raise NotImplementedError("Implement dispatch_tool_call")
