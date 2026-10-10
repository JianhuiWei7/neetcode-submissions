class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) >= 2:
            largest1 = -heapq.heappop(heap)
            largest2 = -heapq.heappop(heap)
            if largest1 > largest2:
                heapq.heappush(heap, -(largest1 - largest2))
            elif largest2 > largest1:
                heapq.heappush(heap, -(largest2 - largest1))
        if len(heap) != 0:
            return -heap[0]
        return 0