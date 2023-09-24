class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for character in s:
            if character in matching:
                stack.append(character)
            else:
                if stack:
                    item = stack.pop()
                    if character != matching[item]:
                        return False
                else:
                    return False
        return stack == []