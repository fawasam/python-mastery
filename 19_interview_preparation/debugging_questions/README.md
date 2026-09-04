# Python Debugging & Troubleshooting Interview Scenarios

## Systematic Debugging Workflow
```text
  Bug Reported → Reproduce Minimally → Traceback Log Inspection → Identify Root Cause → Implement Fix → Regression Test
```

---

### Scenario 1: Memory Leak with Default Mutable Arguments

**Bug Description:**
In a web backend, calling `add_item()` without passing a list causes accumulated items from previous requests to leak across different users!

**Broken Code:**
```python
def add_item(item: str, items_list: list = []) -> list:
    items_list.append(item)
    return items_list
```

**Why it Happens:**
Default arguments in Python are evaluated ONLY ONCE at module load time when the function is defined, NOT at execution time. All function calls reusing default parameters reference the same single list in RAM.

**Fix:**
```python
def add_item(item: str, items_list: list | None = None) -> list:
    if items_list is None:
        items_list = []
    items_list.append(item)
    return items_list
```

---

### Scenario 2: Unhandled Race Condition in Multithreaded Counter

**Bug Description:**
A high-throughput web server increments a request counter across threads, but the final count is consistently smaller than total incoming requests.

**Why it Happens:**
`count += 1` consists of three CPython bytecode instructions (`LOAD_FAST`, `BINARY_OP`, `STORE_FAST`). A thread context switch during execution causes lost updates.

**Fix:**
Use `threading.Lock()` or an atomic counter object:
```python
import threading

lock = threading.Lock()
count = 0

def increment():
    global count
    with lock:
        count += 1
```
