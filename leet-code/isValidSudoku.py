from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        LENGTH = len(board)
        for i in range(LENGTH):
            checkColumn = [0]*(LENGTH + 1)
            checkRow = [0]*(LENGTH + 1)
            for j in range(LENGTH):
                if board[i][j] != ".":
                    checkColumn[int(board[i][j])] += 1
                    if checkColumn[int(board[i][j])] > 1:
                        return False
                if board[j][i] != ".":
                    checkRow[int(board[j][i])] += 1
                    if checkRow[int(board[j][i])] > 1:
                        return False
        for i in range(0, LENGTH, 3):
            for j in range(0, LENGTH, 3):

                checkColumn = [0]*(LENGTH + 1)
                for m in range(i, i + 3):
                    for n in range(j, j + 3):
                        if board[m][n] != ".":
                            checkColumn[int(board[m][n])] += 1
                            if checkColumn[int(board[m][n])] > 1:
                                return False
        return True


print(Solution().isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
      "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
