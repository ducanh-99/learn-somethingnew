class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def checkFrequentlyValid(frequently: dict, current_frequently: dict):
            if len(frequently.keys()) != len(current_frequently.keys()):
                return False
            for key in frequently:
                if key not in current_frequently:
                    return False
                elif current_frequently[key]["count"] < frequently[key]:
                    return False
            return True

        left = right = 0
        frequently = {}
        res = []

        for i in t:
            if i not in frequently:
                frequently[i] = 1
            else:
                frequently[i] += 1
        index_and_count_frequently = {}
        while right < len(s):
            letter = s[right]
            if letter in frequently:
                if letter in index_and_count_frequently:
                    current_frequently = index_and_count_frequently[letter]
                    if current_frequently["count"] == frequently[letter]:
                        index_and_count_frequently[letter]["index"].pop(0)
                        index_and_count_frequently[letter]["index"].append(
                            right)
                        if s[left] == letter:
                            current_left = float("inf")
                            for key in index_and_count_frequently:
                                current_left = min(
                                    index_and_count_frequently[key]["index"][0], current_left)
                            left = current_left
                    else:
                        index_and_count_frequently[letter]["count"] += 1
                        index_and_count_frequently[letter]["index"].append(
                            right)
                else:
                    index_and_count_frequently[letter] = {
                        "index": [right],
                        "count": 1
                    }
                if checkFrequentlyValid(frequently, index_and_count_frequently):
                    current_left = float("inf")
                    for key in index_and_count_frequently:
                        current_left = min(
                            index_and_count_frequently[key]["index"][0], current_left)
                    left = current_left
                    res.append([left, right])
            right += 1

        left_right_res = float("inf")
        left, right = 0, 0
        for index in res:
            if index[1] - index[0] < left_right_res:
                left, right = index
                left_right_res = right - left
        return s[left:right+1] if res else ""


print(Solution().minWindow(
    "a",
    "aa"
)
)
print(Solution().minWindow(
    "ADOBECODEBANC",
    "ABC"
)
)
