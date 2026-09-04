"""
Performance Mini Project: Log Processor Benchmarking & Optimization Suite.

Demonstrates real-world optimization of a high-volume log filtering & processing pipeline.
"""

from functools import lru_cache
import random
import time


class UnoptimizedLogRecord:
    """Standard Python class storing log record attributes in default __dict__."""
    def __init__(self, record_id: int, user_id: int, status_code: int, endpoint: str) -> None:
        self.record_id = record_id
        self.user_id = user_id
        self.status_code = status_code
        self.endpoint = endpoint


class OptimizedLogRecord:
    """Optimized class using __slots__ to eliminate per-instance __dict__ overhead."""
    __slots__ = ("record_id", "user_id", "status_code", "endpoint")
    
    def __init__(self, record_id: int, user_id: int, status_code: int, endpoint: str) -> None:
        self.record_id = record_id
        self.user_id = user_id
        self.status_code = status_code
        self.endpoint = endpoint


# --- Unoptimized Pipeline ---

def unoptimized_pipeline(records: list[UnoptimizedLogRecord], target_users: list[int]) -> dict[str, int]:
    """
    Naive processing pipeline:
    - O(n) list membership lookup 'record.user_id in target_users'
    - Repeated expensive string formatting
    """
    counts: dict[str, int] = {}
    for rec in records:
        # Bad: searching a list inside a loop -> O(n*m)
        if rec.user_id in target_users and rec.status_code >= 400:
            key = f"ERROR:{rec.endpoint.upper()}"
            counts[key] = counts.get(key, 0) + 1
    return counts


# --- Optimized Pipeline ---

@lru_cache(maxsize=128)
def format_error_key(endpoint: str) -> str:
    """Cache string transformations to avoid redundant allocations."""
    return f"ERROR:{endpoint.upper()}"


def optimized_pipeline(records: list[OptimizedLogRecord], target_users: list[int]) -> dict[str, int]:
    """
    Optimized processing pipeline:
    - Set lookup O(1) for target users
    - Cached key formatting
    """
    target_set = set(target_users)  # Convert list to hash set O(m) once
    counts: dict[str, int] = {}
    
    for rec in records:
        # Fast set membership check O(1)
        if rec.status_code >= 400 and rec.user_id in target_set:
            key = format_error_key(rec.endpoint)
            counts[key] = counts.get(key, 0) + 1
            
    return counts


def main() -> None:
    print("=== Generating Synthetic Log Data ===")
    num_records = 100_000
    endpoints = ["/api/v1/login", "/api/v1/users", "/api/v1/checkout", "/api/v1/pay"]
    
    unopt_records = [
        UnoptimizedLogRecord(
            record_id=i,
            user_id=random.randint(1, 5000),
            status_code=random.choice([200, 201, 400, 404, 500]),
            endpoint=random.choice(endpoints)
        )
        for i in range(num_records)
    ]
    
    opt_records = [
        OptimizedLogRecord(
            record_id=r.record_id,
            user_id=r.user_id,
            status_code=r.status_code,
            endpoint=r.endpoint
        )
        for r in unopt_records
    ]
    
    target_users = list(range(100, 600))  # 500 target user IDs
    
    print("\n--- Running Unoptimized Pipeline ---")
    start = time.perf_counter()
    unopt_res = unoptimized_pipeline(unopt_records, target_users)
    unopt_duration = time.perf_counter() - start
    print(f"Time taken: {unopt_duration:.4f} seconds")
    
    print("\n--- Running Optimized Pipeline ---")
    start = time.perf_counter()
    opt_res = optimized_pipeline(opt_records, target_users)
    opt_duration = time.perf_counter() - start
    print(f"Time taken: {opt_duration:.4f} seconds")
    
    assert unopt_res == opt_res, "Pipeline outputs do not match!"
    print(f"\nSUCCESS: Results match! Optimized version is {unopt_duration / opt_duration:.1f}x faster.")


if __name__ == "__main__":
    main()
