"""
Asynchronous Rate-Limited Batch Processing Pipeline.
"""

import asyncio
from unittest.mock import MagicMock
import httpx


# 1. ASYNC HTTP SCRAPER WORKER
async def fetch_target_page(client: httpx.AsyncClient, sem: asyncio.Semaphore, url: str) -> dict[str, str]:
    async with sem:
        print(f"[HTTP GET] Requesting {url}...")
        response = await client.get(url)
        return {"url": url, "status": str(response.status_code)}


# 2. QUEUE CONSUMER WORKER
async def queue_worker(worker_id: int, queue: asyncio.Queue[str], client: httpx.AsyncClient, sem: asyncio.Semaphore, results: list[dict[str, str]]) -> None:
    while True:
        url = await queue.get()
        try:
            res = await fetch_target_page(client, sem, url)
            results.append(res)
            print(f" [WORKER {worker_id}] Successfully processed {url}")
        except Exception as e:
            print(f" [WORKER {worker_id}] Error processing {url}: {e}")
        finally:
            queue.task_done()


# 3. PIPELINE ORCHESTRATOR
async def run_async_pipeline(urls: list[str], max_concurrency: int = 2) -> list[dict[str, str]]:
    queue: asyncio.Queue[str] = asyncio.Queue()
    sem = asyncio.Semaphore(max_concurrency)
    results: list[dict[str, str]] = []

    # Enqueue work items
    for url in urls:
        await queue.put(url)

    # Setup mock client for test execution
    mock_client = MagicMock(spec=httpx.AsyncClient)
    mock_resp = MagicMock()
    mock_resp.status_code = 200

    async def mock_get(target_url: str):
        await asyncio.sleep(0.02)
        return mock_resp

    mock_client.get = mock_get

    # Launch 3 background worker tasks
    workers = [
        asyncio.create_task(queue_worker(i + 1, queue, mock_client, sem, results))
        for i in range(3)
    ]

    # Wait until all queued items are processed
    await queue.join()

    # Cancel workers cleanly
    for w in workers:
        w.cancel()

    return results


if __name__ == "__main__":
    target_urls = [f"https://api.dev.io/resource/{i}" for i in range(1, 6)]

    print(f"--- Launching Async Pipeline for {len(target_urls)} URLs ---")
    output = asyncio.run(run_async_pipeline(target_urls, max_concurrency=2))

    print(f"\nFinal Async Processing Pipeline Completed: {len(output)} records processed.")
    assert len(output) == 5
