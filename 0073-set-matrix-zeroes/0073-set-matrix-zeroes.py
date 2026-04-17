class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        rowsZ = {}
        colsZ = {}

        # store zeros
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rowsZ[row] = 1
                    colsZ[col] = 1
        
        # implement
        for row in range(rows):
            if row in rowsZ:
                matrix[row] = [0] * cols
            else:
                for col in range(cols):
                    if col in colsZ:
                        matrix[row][col] = 0               
                
# Time = O(n^2)
# Space = O(1) - In-place