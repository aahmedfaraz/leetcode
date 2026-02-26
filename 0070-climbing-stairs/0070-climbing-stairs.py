class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1: return n
        n1 = 1
        n2 = 1
        count = 2
        while count <= n:
            n1, n2 = n2, n1 + n2
            count += 1
        return n2