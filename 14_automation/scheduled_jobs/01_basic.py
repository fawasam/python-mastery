"""
Scheduled Jobs Basics: Using standard library sched module.
"""

import sched
import time

s = sched.scheduler(time.time, time.sleep)


def periodic_task(name: str, execution_count: list[int]) -> None:
    """Task function scheduled to run in future."""
    execution_count[0] += 1
    print(f"[{time.strftime('%H:%M:%S')}] Executed scheduled task '{name}' (Run #{execution_count[0]})")


if __name__ == "__main__":
    print("Scheduling tasks to execute in 0.1s and 0.2s...")
    counter = [0]
    
    # Schedule one-off delayed events
    s.enter(0.1, 1, periodic_task, argument=("Health Check", counter))
    s.enter(0.2, 1, periodic_task, argument=("Backup Job", counter))
    
    s.run()
    print("Scheduler completed all pending tasks.")
