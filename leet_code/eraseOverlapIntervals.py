from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        count = 1  # Initialize with the first interval
        end_time = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end_time:
                # Non-overlapping interval found, update end_time
                end_time = intervals[i][1]
                count += 1
        to_remove = len(intervals) - count
        return to_remove
