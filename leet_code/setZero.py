from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        save_index = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    save_index.append([i, j])
        for i,j in save_index:
            for k in range(len(matrix[0])):
                matrix[i][k] = 0
            for m in range(len(matrix)):
                matrix[m][j] = 0


print(Solution().setZeroes(
    [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
))
