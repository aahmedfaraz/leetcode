class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)): # O(n)
            val = abs(nums[i])
            if val >= 0 or val < len(nums):
                nums[val-1] = -1 * abs(nums[val-1])
        for i in range(len(nums)): # O(n)
            if nums[i] > 0:
                res.append(i+1)
        return res
# Time = O(n)
# Space = O(1)