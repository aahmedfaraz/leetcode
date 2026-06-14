class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = sorted(list(set(nums)))
        return a[-3 % len(a)]