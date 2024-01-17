class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        res = [""]*len(s)
        index = 2
        for i in range(len(s)):
            if i-index >= 0:
                if s[i] == s[i-index]:
                    res[i] = s[i-index] + res[i-1] + s[i]
                else:
                    res[i] = s[i]
            else:
                res[i] = s[i]
            index = len(res[i]) + 1
        index = 1
        for i in range(len(s)):
            if i - index >= 0:
                if s[i] == s[i-index]:
                    res[i] = s[i-index] + res[i-1] + s[i]

        value = ""
        for i in res:
            if len(value) < len(i):
                value = i
        return value


print(Solution().longestPalindrome(
    "cbbd"
))
