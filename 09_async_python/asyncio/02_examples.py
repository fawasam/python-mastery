"""
Handling Exception Return Modes in asyncio.gather(return_exceptions=True).
"""

import asyncio


async def task_success() -> str:
    return "SUCCESS_DATA"


async def task_failure() -> str:
    raise ConnectionError("Remote database unreachable")


async def main() -> None:
    # Setting return_exceptions=True prevents one failing task from cancelling other tasks!
    results = await asyncio.gather(task_success(), task_failure(), return_exceptions=True)

    print("Gather Results with Exception Inspection:")
    for idx, res in enumerate(results):
        if isinstance(res, Exception):
            print(f" Task {idx + 1} Failed: {type(res).__name__} -> {res}")
        else:
            print(f" Task {idx + 1} Succeeded: {res}")


if __name__ == "__main__":
    asyncio.run(main())
