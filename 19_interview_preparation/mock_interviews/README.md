# Mock Technical Interviews & Self-Assessment Rubrics

## Interview Evaluation Rubric

| Category | Novice (1-2) | Intermediate (3-4) | Senior / Staff (5) |
|---|---|---|---|
| **Pythonic Syntax** | Uses basic C-style loops | Uses comprehensions & type hints | Uses descriptors, context managers, async, and generators naturally |
| **Problem Solving** | Brute force $O(n^2)$ solutions | Optimal $O(n)$ hash map or two pointer approaches | Discusses space/time trade-offs, edge cases, and streaming bounds |
| **Code Architecture** | Single file script with globals | Basic functions and classes | SOLID, Clean Layering, Dependency Injection, and Repository Patterns |
| **Testing & Edge Cases** | No unit tests written | Basic happy-path tests | Edge case handling, fixtures, mocking, and error propagation assertions |

## Sample Mock Interview Session: Senior Python Developer

**Interviewer:** "Design a real-time rate limiter for an API endpoint handling 10,000 requests/sec."

**Candidate Strategy:**
1. **Clarify Requirements**: Distributed rate limiting across API nodes? What is the limit window (e.g. 100 requests per minute)?
2. **Algorithm Selection**: Sliding Window Counter vs Token Bucket using Redis.
3. **Python Implementation**: Async middleware wrapping FastAPI route execution.
4. **Failure Modes**: What happens if Redis goes offline? Fall back to open access (fail-open) vs local in-memory fallback.
