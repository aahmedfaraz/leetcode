class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
# Time complexity = O(n) due to reverse
# Space complexity = O(1)