class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        stack_sign = []
        my_dict = {
            "(" : ")"
        }
        for i in s:
            if i == " ":
                continue
            if s.lstrip('-').isdigit():
                stack.append(s)
            elif s in my_dict:
                stack_sign.append(s)
            elif s == ")":
                while stack_sign[-1] != "(":
                    first, second = 



print(Solution().calculate(
      "(1+(4+5+2)-3)+(6+8)"
      ))
