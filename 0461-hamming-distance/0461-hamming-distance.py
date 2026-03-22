class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx = bin(x)[2:]
        by = bin(y)[2:]
        limit = min(max(len(bx), len(by)), 32)
        bx = bx.zfill(limit)
        by = by.zfill(limit)
        count = 0
        for i in range(limit):
            if bx[i] != by[i]:
                count += 1
        return count