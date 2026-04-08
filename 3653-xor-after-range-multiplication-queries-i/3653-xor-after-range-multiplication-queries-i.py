class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        for l, r, k, v in queries:
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % (10**9 + 7)
                idx += k
        res = 0
        for num in nums:
            res ^= num
        return res

# Time = O(n x q)
# Space = O(1)