class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1

            if t[i] in t_dict:
                t_dict[t[i]] += 1
            else:
                t_dict[t[i]] = 1

        for key in s_dict:
            if key in t_dict:
                if t_dict[key] != s_dict[key]:
                    return False
            else:
                return False
        for key in t_dict:
            if key in s_dict:
                if t_dict[key] != s_dict[key]:
                    return False
            else:
                return False
        return True

print(Solution().isAnagram(
    "anagram",
    "nagaram"
))
