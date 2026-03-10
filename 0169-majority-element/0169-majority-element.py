class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        i, n = 0, len(nums)
        maxval = 0
        maxcount = 0
        while i < n:
            curr = nums[i]
            start = i
            while i < n and nums[i] == curr:
                i += 1
            distance = i - start
            if distance > maxcount:
                maxcount = distance
                maxval = curr
        return maxval

# time = O(n) + O(n log n) = O(n log n) - two while loops, but traveling each element just one time
# space = O(1)