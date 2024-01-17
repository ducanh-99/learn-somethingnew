from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        res = [[0]*len(i) for i in grid]
        res[0][0] = grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i - 1 < 0 and j - 1 < 0:
                    continue
                if i - 1 < 0:
                    res[i][j] = res[i][j-1] + grid[i][j]
                elif j-1 < 0:
                    res[i][j] = res[i-1][j] + grid[i][j]
                else:
                    res[i][j] = min(res[i-1][j], res[i][j-1]) + grid[i][j]
        print(res)
        return res[-1][-1]


print(Solution().minPathSum(
[[1,2,3],[4,5,6]]
))
