class Solution:
    def smallestIndex(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            s = 0
            for ch in str(nums[i]):
                s += int(ch)
            if s == i:
                return i

        return -1