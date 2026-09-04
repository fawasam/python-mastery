"""
Middleware Exercises.
"""

from typing import Callable


# Exercise 1 (Medium): Header Injection Middleware Wrapper
# Write inject_server_header_middleware(headers: dict[str, str], handler: Callable[[], dict[str, str]]) -> dict[str, str]
# Calls handler(), and adds "Server": "PythonMastery/1.0" to returned dictionary.
def inject_server_header_middleware(handler: Callable[[], dict[str, str]]) -> dict[str, str]:
    raise NotImplementedError("Implement inject_server_header_middleware")
