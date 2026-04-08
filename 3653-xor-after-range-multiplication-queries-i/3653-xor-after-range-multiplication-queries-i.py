class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        mult = [1] * n

        for l, r, k, v in queries:
            for i in range(l, r + 1, k):
                mult[i] = (mult[i] * v) % MOD

        res = 0
        for i in range(n):
            res ^= (nums[i] * mult[i]) % MOD

        return res