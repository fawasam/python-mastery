"""
Advanced Scheduling: Interval Loop Runner with Exception Resilience.
"""

import time


def run_resilient_job(job_func: Callable[[], None], max_runs: int = 3, delay_seconds: float = 0.05) -> int:
    """
    Run job_func repeatedly on an interval, catching exceptions so the runner loop does not crash.
    """
    successful_runs = 0
    for run in range(1, max_runs + 1):
        try:
            job_func()
            successful_runs += 1
        except Exception as err:
            print(f"[Warning] Job run #{run} raised exception: {err}. Retrying next interval...")
            
        time.sleep(delay_seconds)
        
    return successful_runs


if __name__ == "__main__":
    attempt = [0]
    
    def flaky_job() -> None:
        attempt[0] += 1
        if attempt[0] == 2:
            raise RuntimeError("Transient network outage!")
        print(f"Flaky job executed successfully on run #{attempt[0]}")

    completed = run_resilient_job(flaky_job, max_runs=3, delay_seconds=0.01)
    print(f"Resilient runner completed {completed}/3 runs successfully.")
