class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        inputs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in s:
            if i in inputs:
                if stack and stack[-1] == inputs[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

