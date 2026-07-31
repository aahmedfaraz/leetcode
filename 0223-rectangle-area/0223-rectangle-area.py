class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # rectangle 1
        l1 = abs(ax2 - ax1)
        h1 = abs(ay1 - ay2)
        a1 = l1 * h1

        # rectangle 2
        l2 = abs(bx2 - bx1)
        h2 = abs(by1 - by2)
        a2 = l2 * h2

        # overlap
        l3 = max(min(bx2, ax2) - max(ax1, bx1), 0)
        h3 = max(min(by2, ay2) - max(ay1, by1), 0)
        a3 = l3 * h3

        return a1 + a2 - a3
