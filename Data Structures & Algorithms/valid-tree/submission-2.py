from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = list(range(n))
        count = n

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        for a, b in edges:
            root_a = find(a)
            root_b = find(b)

            # 两端已经连通，再添加这条边就形成环
            if root_a == root_b:
                return False

            parent[root_b] = root_a
            count -= 1

        # 没有环，还要确保所有节点连通
        return count == 1