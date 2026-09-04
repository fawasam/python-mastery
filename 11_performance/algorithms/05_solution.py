"""
Solutions: Algorithmic Optimization Exercises.
"""


def two_sum_optimal(nums: list[int], target: int) -> tuple[int, int] | None:
    """
    Find indices of two numbers that sum to target in O(n) time.
    
    Why: Using a hash map stores seen value -> index mappings.
    Complement check 'target - num in seen' takes O(1) time.
    """
    seen: dict[int, int] = {}
    for idx, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], idx)
        seen[num] = idx
    return None


def remove_duplicates_preserve_order(items: list[int]) -> list[int]:
    """
    Remove duplicates from items while preserving original order in O(n) time.
    
    Why: In Python 3.7+, dict keys maintain insertion order.
    dict.fromkeys(items) performs O(1) set insertion for each item and retains order.
    """
    return list(dict.fromkeys(items))


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    res = two_sum_optimal(nums, target)
    print(f"Two Sum result for {nums}, target {target}: {res}")
    
    data = [4, 1, 2, 1, 4, 3, 2]
    dedup = remove_duplicates_preserve_order(data)
    print(f"Deduplicated data preserving order: {dedup}")
