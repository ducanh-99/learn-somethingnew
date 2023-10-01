from typing import List


def is_anagrams(s_dict: dict, t_dict: dict):
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


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in my_dict:
                my_dict[sorted_s].append(s)
            else:
                my_dict[sorted_s] = [s]
        return [my_dict[key] for key in my_dict]


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
