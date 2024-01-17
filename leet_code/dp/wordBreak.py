from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # create a dp table to store results of subproblems
        # value of dp[i] will be true if string s can be segmented
        # into dictionary words from 0 to i.
        dp = [False for i in range(len(s) + 1)]
    
        # dp[0] is true because an empty string can always be segmented.
        dp[0] = True
    
        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j: i] in wordDict:
                    dp[i] = True
                    break
        print(dp)
        
        return dp[len(s)]

print(Solution().wordBreak(
    "leetcode",
    ["leet","code"]
))