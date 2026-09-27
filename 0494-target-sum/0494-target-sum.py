from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n = len(nums)
        
        @lru_cache(maxsize=None)
        def bt(i, summ):
            if i == n:
                return 1 if summ == target else 0

            return (
                bt(i+1, summ + nums[i]) +
                bt(i+1, summ - nums[i])
            )

        return bt(0, 0)