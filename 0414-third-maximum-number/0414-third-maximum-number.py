class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        INF = float('-inf')
        f, s, t = INF, INF, INF

        for num in nums:
            if num > f:
                t = s
                s = f
                f = num
            elif num > s and num < f:
                t = s
                s = num
            elif num > t and num < s:
                t = num
        
        return t if t != INF else f