class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxval = 0
        def dfs(row, col, visited, gold):
            nonlocal maxval
            
            if (row, col) in visited or grid[row][col] == 0:
                maxval = max(maxval, gold)
                return

            visited.add((row, col))
            gold += grid[row][col]
            maxval = max(maxval, gold)

            # up
            if row > 0:
                dfs(row-1, col, visited, gold)
            # down
            if row < (rows-1):
                dfs(row+1, col, visited, gold)
            # left
            if col > 0:
                dfs(row, col-1, visited, gold)
            # right
            if col < (cols-1):
                dfs(row, col+1, visited, gold)

            visited.remove((row, col))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    dfs(row, col, set(), 0)

        return maxval
