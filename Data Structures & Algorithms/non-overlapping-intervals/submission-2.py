class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals = sorted(intervals, key=lambda x: x[0])

        num_delete = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                # 有重叠，删除结束较晚的那个
                num_delete += 1
                end = min(end, intervals[i][1])
            else:
                # 没有重叠，保留当前区间
                end = intervals[i][1]

        return num_delete