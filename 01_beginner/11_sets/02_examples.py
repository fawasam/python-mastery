"""
Topic: O(1) Membership Speed vs O(n) List Search
File: 02_examples.py
"""
import time

def compare_membership_performance() -> None:
    # Creating a large dataset of 1,000,000 items
    data_list = list(range(1000000))
    data_set = set(data_list)
    target = 999999

    # Benchmark List Membership (O(n) Linear Scan)
    start_list = time.perf_counter()
    found_in_list = target in data_list
    time_list = time.perf_counter() - start_list

    # Benchmark Set Membership (O(1) Hash Table Lookup)
    start_set = time.perf_counter()
    found_in_set = target in data_set
    time_set = time.perf_counter() - start_set

    print(f"Target found in list? {found_in_list} (Time: {time_list * 1000:.4f} ms)")
    print(f"Target found in set?  {found_in_set} (Time: {time_set * 1000:.4f} ms)")
    print(f"Set search is roughly {time_list / max(time_set, 1e-9):.1f}x faster!")


if __name__ == "__main__":
    compare_membership_performance()
