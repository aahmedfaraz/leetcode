from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        
        # Step 1: find first decreasing index from right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: if found
        if i >= 0:
            # Step 3: find just larger number
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            
            # Step 4: swap
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 5: reverse remaining part
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1