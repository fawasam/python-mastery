# Advanced Generators and Coroutine Pipelines

## What You Will Learn
- State retention in generator functions (`yield`)
- Two-way communication using `generator.send()`, `generator.throw()`, and `generator.close()`
- Delegating generator execution using `yield from`
- Coroutine-style push/pull data processing pipelines

## Why This Matters
Generators provide $O(1)$ memory stream processing. Advanced generator features (`send`, `yield from`) formed the foundation for Python's modern `asyncio` event loop architecture before native `async`/`await` keywords were introduced.

## Examples
See `01_basic.py` and `02_examples.py` for runnable code.

## Exercises
Complete exercises in `04_exercises.py` and check `05_solution.py`.

## Next Topic
Proceed to `../context_managers/`.
