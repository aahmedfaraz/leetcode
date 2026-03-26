class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] > 0: return 0
        nextNum = nums[0]
        i = 0
        while i < len(nums) and nums[i] == nextNum:
            nextNum = nums[i] + 1
            i += 1
        return nextNum
        