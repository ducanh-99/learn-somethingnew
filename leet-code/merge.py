from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: int(x[0]))
        res = []
        current = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= current[1]:
                current[1] = max(intervals[i][1], current[1])
                current[0] = min(intervals[i][0], current[0])
            else:
                res.append(current)
                current = intervals[i]
        res.append(current)
        return res


print(Solution().merge(
    [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
))
