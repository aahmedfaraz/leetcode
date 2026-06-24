class Solution:
    def arrangeCoins(self, n: int) -> int:
        step = 1
        while n > step:
            n -= step
            if n > step:
                step += 1
        return step