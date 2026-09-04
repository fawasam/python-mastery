"""
Generator-Based Coroutine with .send() Pattern.
"""

from typing import Generator


def generator_coroutine_consumer() -> Generator[None, str, str]:
    """
    Classic generator-based consumer that receives items via .send().
    """
    items: list[str] = []
    print("[CONSUMER] Ready to receive items...")
    try:
        while True:
            received = yield
            items.append(received)
            print(f"[CONSUMER] Appended item: '{received}' (Total count: {len(items)})")
    except GeneratorExit:
        print("[CONSUMER] Received GeneratorExit. Finalizing...")
        return f"Processed {len(items)} item(s)"


def demo_generator_consumer() -> None:
    consumer = generator_coroutine_consumer()
    # Prime the generator to advance to the first yield statement
    next(consumer)

    consumer.send("Data Package 1")
    consumer.send("Data Package 2")
    consumer.close()


if __name__ == "__main__":
    demo_generator_consumer()
