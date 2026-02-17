class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1: return False
        stack = []
        closing = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        
        for br in s:
            if br in '({[':
                stack.append(closing[br])
            elif len(stack) == 0 or br != stack.pop():
                return False

        return False if len(stack) > 0 else True  