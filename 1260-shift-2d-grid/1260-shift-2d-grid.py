class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        rows, cols = len(grid), len(grid[0])
        k %= rows * cols

        if k == 0:
            return grid
        
        res = [([0] * cols) for _ in range(rows)]
        currRow = []
        r, c = k // cols, k % cols

        for row in range(rows):
            for col in range(cols):
                res[r][c] = grid[row][col]
                c += 1
                if c == cols:
                    c = 0
                    r += 1
                if r == rows:
                    r = 0
        
        return res