class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left, right = 0, len(nums)-1
        res = [0] * len(nums)
        i = len(nums)-1

        while left <= right:
            numl = abs(nums[left])
            numr = abs(nums[right])
            if numl > numr:
                res[i] = numl**2
                left += 1
            else:
                res[i] = numr**2
                right -= 1
            i -= 1
        
        return res