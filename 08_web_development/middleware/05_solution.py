"""
Solutions for Middleware Exercises.
"""

from typing import Callable


def inject_server_header_middleware(handler: Callable[[], dict[str, str]]) -> dict[str, str]:
    res = handler()
    res["Server"] = "PythonMastery/1.0"
    return res


def dummy_route() -> dict[str, str]:
    return {"Content-Type": "application/json"}


if __name__ == "__main__":
    wrapped = inject_server_header_middleware(dummy_route)
    assert wrapped["Server"] == "PythonMastery/1.0"
    print("Middleware header injection exercise passed successfully!")
