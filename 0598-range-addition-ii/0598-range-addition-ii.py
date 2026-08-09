class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minx, miny = m, n
        for op in ops:
            x, y = op
            minx = min(x, minx)
            miny = min(y, miny)
        return minx * miny
# Time = O(n)
# Space = O(1)