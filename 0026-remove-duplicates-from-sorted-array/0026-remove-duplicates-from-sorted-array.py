class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 1
        i = 0

        for j, num in enumerate(nums):
            if num == nums[i]:
                continue
            i += 1
            nums[i] = num
        
        return i+1