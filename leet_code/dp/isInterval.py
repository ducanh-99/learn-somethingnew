class Solution:
    def isInterleave(self, A: str, B: str, C: str) -> bool:
        len_A, len_B, len_C = len(A), len(B), len(C)

        if len_A + len_B != len_C:
            return False

        dp = [[False] * (len_B + 1) for _ in range(len_A + 1)]

        for i in range(len_A + 1):
            for j in range(len_B + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and B[j - 1] == C[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and A[i - 1] == C[i + j - 1]
                else:
                    dp[i][j] = (dp[i - 1][j] and A[i - 1] == C[i + j - 1]
                                ) or (dp[i][j - 1] and B[j - 1] == C[i + j - 1])

        return dp[len_A][len_B]


print(Solution().isInterleave(
    "aabccc",
    "dbbca",
    "aadbbcbcacc"
))
