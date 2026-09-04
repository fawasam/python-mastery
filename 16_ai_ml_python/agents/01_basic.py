"""
AI Agents Basics: Tool Registration and Tool Calling Dispatcher.
"""

from typing import Callable, Any

# Tool Registry binding Python functions to tool names
TOOL_REGISTRY: dict[str, Callable[..., str]] = {}


def register_tool(name: str) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        TOOL_REGISTRY[name] = func
        return func
    return decorator


@register_tool("calculator")
def tool_calculator(expression: str) -> str:
    """Evaluate basic arithmetic expressions safely."""
    try:
        allowed_chars = "0123456789+-*/. ()"
        if any(c not in allowed_chars for c in expression):
            return "Error: Invalid characters in math expression"
        return str(eval(expression, {"__builtins__": None}, {}))
    except Exception as e:
        return f"Error: {e}"


@register_tool("get_weather")
def tool_get_weather(city: str) -> str:
    """Fetch current weather for a given city."""
    return f"Weather in {city}: Sunny, 24°C"


def execute_agent_tool_call(tool_name: str, **kwargs: Any) -> str:
    """Dispatch execution to registered agent tool."""
    if tool_name not in TOOL_REGISTRY:
        return f"Error: Tool '{tool_name}' is not registered."
    return TOOL_REGISTRY[tool_name](**kwargs)


if __name__ == "__main__":
    res_calc = execute_agent_tool_call("calculator", expression="45 * 2 + 10")
    res_weather = execute_agent_tool_call("get_weather", city="Tokyo")

    print("Calculator Tool Result:", res_calc)
    print("Weather Tool Result:", res_weather)
