class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        number = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)

            elif ch == '+':
                result += sign * number
                number = 0
                sign = 1

            elif ch == '-':
                result += sign * number
                number = 0
                sign = -1

            elif ch == '(':
                # Save result and sign before entering parentheses
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            elif ch == ')':
                # Finish the number before ')'
                result += sign * number
                number = 0

                # Sign before '('
                sign = stack.pop()

                # Result before '('
                previous_result = stack.pop()

                result = previous_result + sign * result

        # Add the final number
        result += sign * number

        return result