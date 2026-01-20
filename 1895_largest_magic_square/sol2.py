class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # initialize all prefix sum arrays with 0 filled as all values
        row = [[0] * (n + 1) for _ in range(m)]
        col = [[0] * n for _ in range(m + 1)]
        diag1 = [[0] * (n + 1) for _ in range(m + 1)] # left to right
        diag2 = [[0] * (n + 2) for _ in range(m + 1)] # right to left

        # fill prefix sums
        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        def isMagic(r, c, size): # r = curr row, c = curr col, size = square size 
            target = row[r][c + size] - row[r][c]

            # check rows
            for i in range(r, r + size):
                if row[i][c + size] - row[i][c] != target:
                    return False

            # check columns
            for j in range(c, c + size):
                if col[r + size][j] - col[r][j] != target:
                    return False

            # check diagonals
            if diag1[r + size][c + size] - diag1[r][c] != target:
                return False
            if diag2[r + size][c] - diag2[r][c + size] != target:
                return False

            return True

        # loop in decreasing order, so we get the largest square first
        for size in range(min(m, n), 1, -1):
            for i in range(m - size + 1):
                for j in range(n - size + 1):
                    if isMagic(i, j, size):
                        return size

        return 1

# Example usage:
print(Solution().largestMagicSquare([[7,1,4,5,6],
                                     [2,5,1,6,4],
                                     [1,5,4,3,2],
                                     [1,2,7,3,4]]))

print(Solution().largestMagicSquare([[5,1,3,1],
                                     [9,3,3,1],
                                     [1,3,3,8]]))

# Time Complexity:
# Building prefix sums: O(m * n)
# For each possible square size k, we scan all positions O(m * n)
# Each isMagic check costs O(k) for rows + O(k) for columns = O(k)
# Worst-case overall: O(m * n * min(m, n))

# Space Complexity:
# O(m * n) for row, column, and diagonal prefix sum matrices

# OUTPUT:
# 3
# 2