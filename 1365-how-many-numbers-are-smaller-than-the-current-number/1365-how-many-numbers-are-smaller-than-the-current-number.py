from bisect import bisect_left

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)

        return [bisect_left(sorted_nums, num) for num in nums]