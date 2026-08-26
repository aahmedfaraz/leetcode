class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                operator = token
                num1 = stack.pop()
                num2 = stack.pop()
                res = 0

                if operator == '+':
                    res = num2 + num1
                elif operator == '-':
                    res = num2 - num1
                elif operator == '*':
                    res = num2 * num1
                elif operator == '/':
                    res = num2 / num1

                stack.append(int(res))
        
        return stack[0]