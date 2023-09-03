class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        res = [[0]*(n+1) for i in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    res[i][j] = 0
                elif text1[i-1] == text2[j-1]:
                    res[i][j] = res[i-1][j-1]+1
                else:
                    res[i][j] = max(res[i-1][j], res[i][j-1])
        print(res)
        return res[-1][-1]