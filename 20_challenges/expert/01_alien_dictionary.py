"""
Challenge 01: Alien Dictionary

Difficulty: ⭐⭐⭐⭐⭐
Topics: Topological Sort, Graph Cycle Detection

Problem:
There is a new alien language that uses the Latin alphabet. However, the order among letters is unknown to you.
You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.
Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules. If there is no possible order, return "".
"""

from collections import defaultdict, deque


def alien_order(words: list[str]) -> str:
    adj: dict[str, set[str]] = {char: set() for word in words for char in word}
    in_degree = {char: 0 for char in adj}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        
        # Check invalid prefix ordering (e.g. ["abc", "ab"])
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
            
        for j in range(min_len):
            if w1[j] != w2[j]:
                if w2[j] not in adj[w1[j]]:
                    adj[w1[j]].add(w2[j])
                    in_degree[w2[j]] += 1
                break

    # Topological Sort via Kahn's Algorithm (BFS)
    queue = deque([char for char in in_degree if in_degree[char] == 0])
    res = []

    while queue:
        char = queue.popleft()
        res.append(char)
        for neighbor in adj[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return "".join(res) if len(res) == len(adj) else ""


if __name__ == "__main__":
    alien_words = ["wrt", "wrf", "er", "ett", "rftt"]
    print("Alien Dictionary Character Order:", alien_order(alien_words))
