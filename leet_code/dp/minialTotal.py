from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = []
        for i in range(len(triangle)):
            res.append([0]*len(triangle[i]))
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                if i == 0:
                    res[i][j] = triangle[i][j]
                else:

                    print(
                        res[i-1][j] if j < len(triangle[i-1]
                                               ) else float("-inf"),
                        res[i-1][j-1] if j > 0 else float("-inf")
                    )
                    res[i][j] = min(
                        res[i-1][j] if j < len(triangle[i-1]
                                               ) else float("inf"),
                        res[i-1][j-1] if j > 0 else float("inf")
                    ) + triangle[i][j]
        return min(res[-1])


print(Solution().minimumTotal(
    [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
))
