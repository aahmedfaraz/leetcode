class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        def sq(num):
            return num**2
        return sorted(list(map(sq, nums)))