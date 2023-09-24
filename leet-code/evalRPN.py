from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = [] 
        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                first, second = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(second+first)
                if token == "-":
                    stack.append(second-first)
                if token =="*":
                    stack.append(second*first)
                if token =="/":
                    stack.append(int(second/first))
        return stack[-1]

print(Solution().evalRPN(
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
)) 