class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[0])
        num_delete = 0
        for i in range(len(intervals)):
            
            while i + 1 < len(intervals) and intervals[i][1] > intervals[i+1][0]:
                if intervals[i][1] > intervals[i+1][1]:
                    # remove i
                    del intervals[i]
                else:
                    del intervals[i+1]
                num_delete += 1
        return num_delete
