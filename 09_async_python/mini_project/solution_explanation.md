# Solution Explanation: Asynchronous Rate-Limited Batch Processing Pipeline

## Architecture Overview

1. **`asyncio.Queue` Decoupling**:
   Items are enqueued by the producer without blocking. Multiple worker tasks pop items concurrently.

2. **`asyncio.Semaphore` Throttling**:
   Limits outbound HTTP request concurrency ceiling regardless of total worker count, preventing API rate limit blocks.

3. **`queue.join()` & Clean Worker Cancellation**:
   Awaits `queue.join()` until every task signals `queue.task_done()`, then cleanly cancels background worker loops.
