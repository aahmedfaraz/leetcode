import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 3: return n == 1
        start = 3
        while start < n:
            start *= 3
        return start == n