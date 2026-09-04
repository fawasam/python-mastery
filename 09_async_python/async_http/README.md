# Asynchronous HTTP Clients (`httpx.AsyncClient`) in Python

## What You Will Learn
* Asynchronous HTTP requests using `httpx.AsyncClient()`.
* Concurrent API scraping and batch fetching.
* Managing connection pools with `async with httpx.AsyncClient()`.
* Rate limiting and batching async HTTP requests with `asyncio.Semaphore`.

## Why This Matters
Synchronous HTTP clients process requests one after another. If each request takes 200ms, 100 requests take 20 seconds. An asynchronous HTTP client handles all 100 requests concurrently over a shared connection pool, finishing in ~200ms total!

## Prerequisites
* HTTP Requests (`08_web_development/requests`)
* Async Await (`09_async_python/async_await`)

## Core Concepts

### Async HTTP Client Pattern
```python
import asyncio
import httpx

async def fetch_page(client: httpx.AsyncClient, url: str) -> dict:
    response = await client.get(url)
    return response.json()

async def main():
    urls = ["https://httpbin.org/get?id=1", "https://httpbin.org/get?id=2"]
    async with httpx.AsyncClient(timeout=5.0) as client:
        tasks = [fetch_page(client, url) for url in urls]
        results = await asyncio.gather(*tasks)
```

## Exercises
See `04_exercises.py` to practice concurrent URL fetching.
