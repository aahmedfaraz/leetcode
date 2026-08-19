class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        num = 0
        sign = 1
        prevResults = []

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '+':
                result += sign * num
                num = 0
                sign = 1
            elif ch == '-':
                result += sign * num
                num = 0
                sign = -1
            elif ch == '(':
                prevResults.append(result)
                prevResults.append(sign)
                result = 0
                sign = 1
            elif ch == ')':
                result += sign * num
                num = 0
                sign = 1

                prevSign = prevResults.pop()
                prevRes = prevResults.pop()

                result = prevRes + (prevSign * result)
        
        result += sign * num

        return result
