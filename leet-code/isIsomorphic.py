class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t, t_to_s = {}, {}
        for s_char, t_char in zip(s, t):
            if s_char not in s_to_t:
                s_to_t[s_char] = t_char
            else:
                if s_to_t[s_char] != t_char:
                    return False
            if t_char not in t_to_s:
                t_to_s[t_char] = s_char
            else:
                if t_to_s[t_char] != s_char:
                    return False
        return True




print(Solution().isIsomorphic(
    "bbbaaaba",
    "aaabbbba"
))
