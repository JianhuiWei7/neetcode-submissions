class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        heap = [(0,0)]
        total_cost = 0
        while heap:
            cost,node = heapq.heappop(heap)
            if node in visited:
                continue
            total_cost += cost
            x1,y1 = points[node]
            visited.add(node)
            for index in range(len(points)):
                if index in visited:
                    continue
                x2,y2 = points[index]
                distance = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(heap,(distance, index))
        return total_cost
                