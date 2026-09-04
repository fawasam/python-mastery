"""
Solutions for HTTP Exercises.
"""


def categorize_status_code(code: int) -> str:
    if 100 <= code < 200:
        return "INFORMATIONAL"
    elif 200 <= code < 300:
        return "SUCCESS"
    elif 300 <= code < 400:
        return "REDIRECT"
    elif 400 <= code < 500:
        return "CLIENT_ERROR"
    elif 500 <= code < 600:
        return "SERVER_ERROR"
    return "UNKNOWN"


if __name__ == "__main__":
    assert categorize_status_code(200) == "SUCCESS"
    assert categorize_status_code(404) == "CLIENT_ERROR"
    assert categorize_status_code(503) == "SERVER_ERROR"
    print("HTTP status code categorization exercise passed successfully!")
