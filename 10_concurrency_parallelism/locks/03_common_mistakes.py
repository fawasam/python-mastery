"""
Common Mistakes in Locking: Deadlocks.
"""

import threading


# MISTAKE 1: Deadlock due to inconsistent lock acquisition order
def mistake_deadlock() -> None:
    # Thread 1 acquires Lock A then Lock B
    # Thread 2 acquires Lock B then Lock A
    # If both threads run simultaneously, Thread 1 waits for B while Thread 2 waits for A -> DEADLOCK!
    pass


if __name__ == "__main__":
    print("Always acquire multiple locks in a global, consistent order across all threads to prevent deadlocks!")
