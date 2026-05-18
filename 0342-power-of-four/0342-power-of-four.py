import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1: return True
        if n < 4: return False
        ans = math.log(n, 4)
        return (ans - int(ans)) == 0