class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) > 1:
            i, j = 0, 1
            while i < len(nums) and j < len(nums):
                if nums[i] == 0 and nums[j] != 0:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp

                if nums[i] != 0:
                    i += 1

                j += 1

# Time complexity = O(n)
# Space complexity = O(1)