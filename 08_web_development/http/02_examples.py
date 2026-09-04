"""
Parsing HTTP Headers and URL Query Parameters.
"""

from urllib.parse import parse_qs, urlparse


def parse_request_url(full_url: str) -> tuple[str, dict[str, list[str]]]:
    parsed = urlparse(full_url)
    endpoint_path = parsed.path
    query_params = parse_qs(parsed.query)
    return endpoint_path, query_params


if __name__ == "__main__":
    test_url = "https://api.example.com/v1/users?page=2&limit=50&sort=desc"
    path, params = parse_request_url(test_url)

    print(f"Target Path: {path}")
    print(f"Query Parameters: {params}")
    assert params["page"] == ["2"]
    assert params["limit"] == ["50"]
