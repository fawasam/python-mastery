"""
Practical Weak Reference Caching Example.
"""

import weakref


class LargeDataObject:
    def __init__(self, data_id: str) -> None:
        self.data_id = data_id
        # Imagine allocating 50MB of payload data here
        self.payload = f"Payload for {data_id}"

    def __repr__(self) -> str:
        return f"<LargeDataObject {self.data_id}>"


class WeakCache:
    """
    Cache holding weak references to objects. When caller drops all strong references,
    cached objects are garbage collected automatically without explicit eviction logic!
    """

    def __init__(self) -> None:
        self._cache: weakref.WeakValueDictionary[str, LargeDataObject] = weakref.WeakValueDictionary()

    def get(self, data_id: str) -> LargeDataObject:
        if data_id in self._cache:
            print(f"[CACHE HIT] Returning cached object for {data_id}")
            return self._cache[data_id]

        print(f"[CACHE MISS] Instantiating new LargeDataObject for {data_id}")
        obj = LargeDataObject(data_id)
        self._cache[data_id] = obj
        return obj

    def size(self) -> int:
        return len(self._cache)


if __name__ == "__main__":
    cache = WeakCache()

    # Create a strong reference in caller scope
    item1 = cache.get("dataset_A")
    print(f"Cache size: {cache.size()}")

    # Accessing again hits the cache
    item1_again = cache.get("dataset_A")

    # Drop all strong references to dataset_A
    print("\n--- Dropping strong references to item1 ---")
    del item1
    del item1_again

    # Notice cache automatically evicted the deallocated object!
    print(f"Cache size after dropping references: {cache.size()}")
