class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dup, mis = -1, -1

        # find duplicate using same memory
        for num in nums:
            ind = abs(num) - 1
            if dup < 0 and nums[ind] < 0:
                dup = abs(num)
            if nums[ind] > 0:
                nums[ind] *= -1
        
        # find missing
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                mis = i
        
        if mis == -1:
            mis = len(nums)
            
        return [dup, mis]