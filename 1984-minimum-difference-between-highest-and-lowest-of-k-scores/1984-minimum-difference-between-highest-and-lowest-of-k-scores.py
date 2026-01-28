from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:  # Only one element, difference is 0
            return 0
        
        nums.sort() # O(n log n)
        n = len(nums)
        min_diff = float('inf')
        
        for i in range(n - k + 1): # O(n)
            current_diff = nums[i + k - 1] - nums[i]
            min_diff = min(min_diff, current_diff)
        
        return min_diff

# Time complexity = O(n log n)
# space = O(1)