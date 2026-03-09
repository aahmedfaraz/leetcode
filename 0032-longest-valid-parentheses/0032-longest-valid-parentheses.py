import math

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        open_bracket, close_bracket, max_val = 0, 0, 0
        for char in s:
            if char == '(':
                open_bracket += 1
            else:
                close_bracket += 1
            
            if open_bracket == close_bracket:
                max_val = max(max_val, open_bracket * 2)
            elif close_bracket > open_bracket:
                open_bracket, close_bracket = 0, 0
        
        open_bracket, close_bracket = 0, 0                
        for char in s[::-1]:
            if char == ')':
                open_bracket += 1
            else:
                close_bracket += 1
            
            if open_bracket == close_bracket:
                max_val = max(max_val, open_bracket * 2)
            elif close_bracket > open_bracket:
                open_bracket, close_bracket = 0, 0
        
        return max_val

