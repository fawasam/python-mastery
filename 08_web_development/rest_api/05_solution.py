"""
Solutions for REST API Exercises.
"""


def resolve_rest_status(method: str, is_created: bool = False) -> int:
    m = method.upper()
    if m == "POST":
        return 201 if is_created else 200
    elif m in ("GET", "PUT", "PATCH"):
        return 200
    elif m == "DELETE":
        return 204
    return 405


if __name__ == "__main__":
    assert resolve_rest_status("POST", is_created=True) == 201
    assert resolve_rest_status("GET") == 200
    assert resolve_rest_status("DELETE") == 204
    assert resolve_rest_status("TRACE") == 405
    print("REST verb resolver exercise passed successfully!")
