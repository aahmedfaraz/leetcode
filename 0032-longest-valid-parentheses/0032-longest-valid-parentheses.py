import math

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxval = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxval = max(maxval, i - stack[len(stack)-1])
        return maxval