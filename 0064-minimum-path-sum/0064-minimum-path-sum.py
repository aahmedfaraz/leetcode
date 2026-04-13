class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        INF = float('inf')
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    continue
                grid[row][col] += min(grid[row-1][col] if row > 0 else INF, grid[row][col-1] if col > 0 else INF)
        
        return grid[rows-1][cols-1]