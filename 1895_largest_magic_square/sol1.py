class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        gridRows = len(grid)
        gridCols = len(grid[0])
        maxSize = 0

        if gridRows == 0 and gridCols == 0: return 0
        if gridRows == 1 and gridCols == 1: return 1

        # Check all possible squares of size 2 up to gridRows
        for size in range(2, min(gridRows, gridCols) + 1):
            for row in range(gridRows - size + 1):
                for col in range(gridCols - size + 1):
                    if self.isMagicSquare(row, col, size, grid):
                        maxSize = max(size, maxSize)
        return 1 if maxSize == 0 else maxSize
    
    def isMagicSquare(self, i: int, j: int, size: int, grid: List[List[int]]) -> bool:
        row = i
        col = j
        mainSum = 0

        rowsToConsider = grid[i: i+size]
        square = []

        # Create Square + Check Rows
        for row in rowsToConsider:
            trimmedRow = row[j: j+size]
            square.append(trimmedRow)
            currRowSum = sum(trimmedRow)
            if mainSum != 0 and currRowSum != mainSum:
                return False
            elif mainSum == 0:
                mainSum = currRowSum
        
        # Check Cols and Diagonals
        colSums = square[0].copy()
        diagonalSums = [0, 0] # L->R , L<-R
        for i, row in enumerate(square):
            if i == 0:
                diagonalSums[0] += row[0]
                diagonalSums[1] += row[-1]
                if diagonalSums[0] > mainSum or diagonalSums[1] > mainSum:
                    return False
                continue
            
            # Fill Diagonals
            diagonalSums[0] += row[i]
            diagonalSums[1] += row[size-1-i]

            if diagonalSums[0] > mainSum or diagonalSums[1] > mainSum:
                return False

            # Fill Cols
            for j, num in enumerate(row):
                colSums[j] += num
                if colSums[j] > mainSum:
                    return False
        
        # Check Diagonals
        if diagonalSums[0] != mainSum or diagonalSums[1] != mainSum:
            return False
        # Check Cols
        for colSum in colSums:
            if colSum != mainSum:
                return False

        return True

# Example usage:
Solution().largestMagicSquare([[7,1,4,5,6],
                               [2,5,1,6,4],
                               [1,5,4,3,2]])
Solution().largestMagicSquare([[5,1,3,1],
                               [9,3,3,1],
                               [1,3,3,8]])

# Time Complexity: O(n^3 * m^3) in the worst case, where n = number of rows, m = number of columns.
# Space Complexity: O(size^2) for the temporary `square` array in `isMagicSquare` function.

# OUTPUT:
# 3
# 2
