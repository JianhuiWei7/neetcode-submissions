from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        count = n

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        for a, b in edges:
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                parent[root_b] = root_a
                count -= 1

        return count