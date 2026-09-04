"""
Common Mistakes in Parallel Processing.
"""


# MISTAKE 1: Over-chunking datasets with tiny tasks
def mistake_tiny_chunks() -> None:
    # DANGER: Spawning 100,000 separate processes to compute 1 + 1 incurs massive process creation overhead!
    # IPC and serialization costs far exceed the tiny calculation time!
    pass


if __name__ == "__main__":
    print("Balance process pool worker count and chunk size so inter-process overhead does not outweigh computation!")
