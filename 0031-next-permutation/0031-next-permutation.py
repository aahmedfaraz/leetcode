class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        # Find decreasing sequence
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            # Find 1st larger number from right
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            # Swap 
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse rest of the array
        nums[i+1:] = nums[i+1:][::-1]

# Time = O(n)
# Space = O(1)