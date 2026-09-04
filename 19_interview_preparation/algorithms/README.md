# Core Algorithms & Complexity Matrix

## Essential Algorithms

### 1. Binary Search
**Time Complexity:** $\mathcal{O}(\log n)$ | **Space:** $\mathcal{O}(1)$
```python
def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### 2. Breadth-First Search (BFS Graph Traversal)
**Time Complexity:** $\mathcal{O}(V + E)$ | **Space:** $\mathcal{O}(V)$
```python
from collections import deque

def bfs(graph: dict[str, list[str]], start: str) -> list[str]:
    visited: set[str] = {start}
    queue: deque[str] = deque([start])
    traversal: list[str] = []
    
    while queue:
        node = queue.popleft()
        traversal.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return traversal
```

### 3. Depth-First Search (DFS Graph Traversal)
**Time Complexity:** $\mathcal{O}(V + E)$ | **Space:** $\mathcal{O}(V)$
```python
def dfs(graph: dict[str, list[str]], start: str, visited: set[str] | None = None) -> list[str]:
    if visited is None:
        visited = set()
    visited.add(start)
    traversal = [start]
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            traversal.extend(dfs(graph, neighbor, visited))
            
    return traversal
```
