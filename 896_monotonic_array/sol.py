class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        size = len(nums)
        if size == 1: return True

        curr = 0
        tone = 0 # 0 -> neutral, 1 -> dec , 2 -> inc

        while curr < size - 1:
            if nums[curr] == nums[curr+1]:
                curr +=1 
                continue

            if tone == 0:
                tone = 1 if nums[curr] > nums[curr+1] else 2
            
            if (nums[curr] > nums[curr+1] and tone == 2) or (nums[curr] < nums[curr+1] and tone == 1):
                return False
            
            curr += 1
        return True


# Example usage:
print(Solution().isMonotonic([1, 2, 2, 3]))
print(Solution().isMonotonic([6, 5, 4, 4]))
print(Solution().isMonotonic([1, 3, 2]))
print(Solution().isMonotonic([1, 2, 4, 5]))
print(Solution().isMonotonic([1, 1, 1]))


# Time Complexity:
# O(n), where n is the length of the array.
# We traverse the array once.

# Space Complexity:
# O(1), only constant extra variables are used.

# OUTPUT:
# True
# True
# False
# True
# True
