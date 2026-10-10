class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_stack = []
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(min_stack, (distance, point[0], point[1]))
        return_list = []
        for _ in range(k):
            _,x,y = heapq.heappop(min_stack)
            return_list.append([x,y])
        return return_list