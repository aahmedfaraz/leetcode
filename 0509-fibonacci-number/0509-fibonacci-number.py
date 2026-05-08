class Solution:
    def fib(self, n: int) -> int:
        num1 = 0
        num2 = 1
        if n < 2: return n
        for _ in range(2, n+1):
            temp = num2
            num2 = num1 + num2
            num1 = temp
        return num2