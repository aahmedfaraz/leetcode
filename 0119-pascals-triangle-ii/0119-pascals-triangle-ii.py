import math

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex+1):
            row.append(math.comb(rowIndex, i))
        return row
