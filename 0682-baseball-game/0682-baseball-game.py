class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for num in operations:
            if num == '+':
                n = len(stack)
                stack.append(stack[n-1] + stack[n-2])
            elif num == 'D':
                n = len(stack)
                stack.append(stack[n-1] * 2)
            elif num == 'C':
                stack.pop()
            else:
                stack.append(int(num))
        
        return sum(stack)

# Time = O(n)
# Space = O(n)  