"""
Challenge 01: Group Anagrams

Difficulty: ⭐⭐⭐
Topics: Dictionaries, Hashing, Strings

Problem:
Given an array of strings strs, group the anagrams together.

Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Expected Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

Constraints:
- 1 <= strs.length <= 10^4

Hints:
- Sorted character tuples make ideal hash map keys!
"""

from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagrams: dict[tuple[str, ...], list[str]] = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())


if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Grouped Anagrams:", group_anagrams(words))
