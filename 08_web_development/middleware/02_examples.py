"""
Rate Limiting Middleware Pattern Simulation.
"""

from typing import Callable


class RateLimitMiddleware:
    def __init__(self, max_requests: int = 3) -> None:
        self.max_requests = max_requests
        self.request_counts: dict[str, int] = {}

    def __call__(self, client_ip: str, next_handler: Callable[[], str]) -> str:
        current_count = self.request_counts.get(client_ip, 0)
        if current_count >= self.max_requests:
            return "429 TOO MANY REQUESTS: Rate limit exceeded"

        self.request_counts[client_ip] = current_count + 1
        return next_handler()


def sample_handler() -> str:
    return "200 OK: Data payload"


if __name__ == "__main__":
    limiter = RateLimitMiddleware(max_requests=2)
    client_ip = "192.168.1.50"

    print(limiter(client_ip, sample_handler))  # 1st call -> Allowed
    print(limiter(client_ip, sample_handler))  # 2nd call -> Allowed
    print(limiter(client_ip, sample_handler))  # 3rd call -> Blocked 429
