class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        result_interval = []
        for i,_ in enumerate(range(len(intervals))):
            while i+1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]:
                intervals[i] = [intervals[i][0], max(intervals[i][1], intervals[i+1][1])]
                del intervals[i + 1] 
        return intervals
