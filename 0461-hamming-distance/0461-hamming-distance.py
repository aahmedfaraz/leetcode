class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bx = bin(x)[2:].zfill(32)
        by = bin(y)[2:].zfill(32)
        count = 0
        for i in range(32):
            if bx[i] != by[i]:
                count += 1
        return count