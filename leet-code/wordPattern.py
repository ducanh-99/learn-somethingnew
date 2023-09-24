class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_s, s_to_pattern = {}, {}
        for pattern_char, word in zip(pattern, s.split(" ")):
            if pattern_char not in pattern_to_s:
                pattern_to_s[pattern_char] = word
            else:
                if pattern_to_s[pattern_char] != word:
                    return False
            if word not in s_to_pattern:
                s_to_pattern[word] = pattern_char
            else:
                if s_to_pattern[word] != pattern_char:
                    return False
        return True


print(Solution().wordPattern(
    "aaaa",
    "dog cat cat dog"
))
