from typing import List

class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        start, end = newInterval

        # 1. 完全位于新区间左边
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # 2. 合并所有重叠区间
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        result.append([start, end])

        # 3. 剩余区间都在右边
        while i < n:
            result.append(intervals[i])
            i += 1

        return result