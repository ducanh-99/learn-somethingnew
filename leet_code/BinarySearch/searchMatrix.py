from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_rows, right_rows = 0, len(matrix)
        row = 0
        while left_rows < right_rows:
            mid = (left_rows + right_rows) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                row = mid
                break
            elif matrix[mid][0] > target:
                right_rows = mid
            else:
                left_rows = mid + 1
        left_c, right_c = 0, len(matrix[0])
        while left_c < right_c:
            mid = (left_c + right_c) // 2
            if matrix[row][mid] < target:
                left_c = mid + 1
            elif matrix[row][mid] > target:
                right_c = mid
            else:
                return True

        print(left_c, right_c)
        print(row, left_rows, right_rows)
        return False


print(Solution().searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
    1
))
