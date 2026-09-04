"""
Basic HTTP Response Processing Simulation.
"""

from dataclasses import dataclass, field


@dataclass
class HTTPResponse:
    status_code: int
    headers: dict[str, str] = field(default_factory=dict)
    body: str = ""

    @property
    def is_success(self) -> bool:
        return 200 <= self.status_code < 300


def handle_http_response(response: HTTPResponse) -> str:
    if response.is_success:
        return f"200 OK SUCCESS: {response.body}"
    elif response.status_code == 404:
        return "404 NOT FOUND: Requested resource does not exist"
    elif response.status_code >= 500:
        return f"500 SERVER ERROR: Remote server failed (Code {response.status_code})"
    return f"HTTP ERROR: Code {response.status_code}"


if __name__ == "__main__":
    res_ok = HTTPResponse(status_code=200, body='{"status": "active"}')
    print(handle_http_response(res_ok))

    res_404 = HTTPResponse(status_code=404)
    print(handle_http_response(res_404))
