# Mini Project: Asynchronous Web Scraping & Event Queue Engine

## Overview
This mini project combines key async programming concepts into a production-style background job processor:
1. **Producer-Consumer Queues (`asyncio.Queue`)**: Decouples URL scraping tasks from data processing workers.
2. **Concurrency Ceiling (`asyncio.Semaphore`)**: Rate-limits concurrent outbound HTTP client calls.
3. **Task Lifecycle Control**: Graceful shutdown and `queue.join()` queue drain verification.

## How to Run
Run the async queue processor using Python:
```bash
python main.py
```
