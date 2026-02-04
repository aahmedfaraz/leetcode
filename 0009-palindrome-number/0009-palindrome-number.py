class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = str(x)

        if len(nums) == 1: return True
        if len(nums) == 2 and nums[0] == nums[1]: return True
        
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] == nums[right]:
                left += 1
                right -= 1
                continue
            return False
        return True
# Time complexity = O(n) due to reverse
# Space complexity = O(1)