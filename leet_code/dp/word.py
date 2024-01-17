from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [False]*(len(s) + 1)
        res[0] = True
        for i in range(len(s)+1):
            for j in range(i):
                if res[j] and s[j:i] in wordDict:
                    res[i] = True

        return res[len(s)]

print(Solution().wordBreak(
    "leetcode",
    ["leet","code"]
))