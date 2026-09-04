# Python System Design & Architecture Interviews

## System Design Blueprint

```text
 Client (Web/Mobile) → [ Load Balancer / Nginx ] → [ FastAPI App Nodes ] → [ Redis Cache ]
                                                         ↓
                                                 [ PostgreSQL DB ] (Primary / Read Replica)
                                                         ↓
                                                 [ Celery / Task Workers ]
```

## Key Topics

### 1. Scaling Python Web Services
- **WSGI / ASGI**: Use Gunicorn with Uvicorn worker processes (`uvicorn.workers.UvicornWorker`).
- **Database Connection Pooling**: Configure SQLAlchemy connection pool sizes (`pool_size=20`, `max_overflow=10`).
- **Async I/O vs Thread Pools**: Use `async def` for network/DB I/O, delegate CPU-intensive tasks to Celery/Multiprocessing worker pools.

### 2. Caching Strategies
- **Cache-Aside Pattern**: Query Redis first; on cache miss, query DB and populate cache with TTL.
- **Write-Through / Write-Back**: Write updates to cache and DB atomically.

### 3. Rate Limiting & API Throttling
- **Sliding Window Log / Leaky Bucket**: Implement token bucket algorithm in Redis to enforce per-IP rate limits (e.g. 100 requests / minute).
