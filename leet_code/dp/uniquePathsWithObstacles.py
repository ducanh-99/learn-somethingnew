from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        res = [[0]*len(i) for i in obstacleGrid]
        res[0][0] = 1

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[i])):
                if obstacleGrid[i][j] == 1:
                    res[i][j] = 0
                    continue
                if i - 1 < 0 and j - 1 < 0:
                    continue
                if i - 1 < 0:
                    res[i][j] = res[i][j-1]
                elif j-1 < 0:
                    res[i][j] = res[i-1][j]
                else:
                    res[i][j] = res[i-1][j] + res[i][j-1]
        print(res)


print(Solution().uniquePathsWithObstacles(
    [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]]
))
