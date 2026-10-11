import heapq
from typing import List

class Solution:
    def networkDelayTime(
        self, times: List[List[int]], n: int, k: int
    ) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, time in times:
            graph[u].append((time, v))

        heap = [(0, k)]
        total_time = 0
        visited = set()

        while heap:
            time, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            total_time = max(total_time, time)

            for travel_time, neighbor in graph[node]:
                if neighbor in visited:
                    continue

                heapq.heappush(
                    heap, (time + travel_time, neighbor)
                )

        return total_time if len(visited) == n else -1