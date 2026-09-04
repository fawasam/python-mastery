"""
Common Misconceptions About Python Internals.
"""

import timeit


# MISCONCEPTION: Assuming list comprehension vs map/filter has identical bytecode performance
def demo_comprehension_vs_map() -> None:
    # List comprehension compiles down to efficient single C-loop bytecode (BUILD_LIST + FOR_ITER)
    comp_time = timeit.timeit("[x * 2 for x in range(1000)]", number=10000)
    # Map requires function call overhead for each element unless using lambda or C builtins
    map_time = timeit.timeit("list(map(lambda x: x * 2, range(1000)))", number=10000)

    print(f"List Comprehension Time: {comp_time:.4f}s")
    print(f"Map with Lambda Time: {map_time:.4f}s")


if __name__ == "__main__":
    demo_comprehension_vs_map()
