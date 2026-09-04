"""
Common Mistakes in Multiprocessing.
"""


# MISTAKE 1: Attempting to share mutable global variables across processes
GLOBAL_COUNTER = 0


def worker_task() -> None:
    global GLOBAL_COUNTER
    # DANGER: Processes DO NOT share global memory address space!
    # Mutating GLOBAL_COUNTER inside a separate process alters ONLY that process's memory copy!
    GLOBAL_COUNTER += 1


if __name__ == "__main__":
    print("Processes have isolated memory address spaces! Use multiprocessing.Queue or Value/Array for IPC state sharing.")
