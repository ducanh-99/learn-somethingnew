from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:

            # if the greatest element in interval is smaller than min of newInterval continue
            if interval[1] < newInterval[0]:
                result.append(interval)

            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval

            elif interval[0] <= newInterval[1] or interval[1] >= newInterval[0]:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        result.append(newInterval)

        return result


print(Solution().insert(
    [[1, 3], [6, 9]],
    [2, 5]
))
