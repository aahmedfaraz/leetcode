import math
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        res = math.log(n, 3)
        rounded = round(res)
        diff = (rounded - res) if rounded >= res else res - rounded
        print(res, rounded, diff)
        return diff >= 0 and diff <= 1e-12