import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        even = False
        if len(num) % 2 == 0: even = True

        mid = math.floor(len(num)) # 8 -> 8/2 -> 4 | 9 -> 9/2 -> 4.5 -> 4
        left = num[:mid]
        right = num[mid if even else mid+1::-1]
        return left == right
#         nums = str(x)

#         if len(nums) == 1: return True
#         if len(nums) == 2 and nums[0] == nums[1]: return True

#         left, right = 0, len(nums) - 1
#         while left < right:
#             if nums[left] == nums[right]:
#                 left += 1
#                 right -= 1
#                 continue
#             return False
#         return True
# # Time complexity = O(n) due to reverse
# # Space complexity = O(1)