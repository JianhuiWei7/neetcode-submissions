from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        # 初始时，每个节点各自属于一个集合
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            # 向上找根，同时缩短路径
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            # 已经连通，添加这条边会形成环
            if root_a == root_b:
                return False

            # 把较小的集合接到较大的集合上
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a

            parent[root_b] = root_a
            size[root_a] += size[root_b]
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]

        return []