import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        return num == num[::-1]
# Time complexity = O(n) due to reverse
# Space complexity = O(1)