class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # replace negatives with neutral value
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # use input array as memory
        for i in range(len(nums)):
            actual_val = abs(nums[i])
            if 0 < actual_val <= len(nums):
                its_place = actual_val-1
                # make place negative, so we know that num exist
                if nums[its_place] > 0:
                    nums[its_place] *= -1
                elif nums[its_place] == 0:
                    nums[its_place] = -1 * (len(nums)+1)
        
        # find missing piece (like jumanji)
        for num in range(1, len(nums)+1):
            if nums[num-1] >= 0:
                return num
        
        return len(nums) + 1
