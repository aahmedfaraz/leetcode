class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1

        if digits[n] != 9:
            digits[n] = digits[n] + 1
            return digits

        while n >= 0 and digits[n] == 9:
            digits[n] = 0
            n -= 1

        if n == -1:
            return [1, *digits]
        else:
            digits[n] = digits[n] + 1
            return digits

# time complexity = O(n)
# space complexity = O(1) - doing in-place update