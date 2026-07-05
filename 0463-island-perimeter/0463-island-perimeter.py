from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols, par = len(grid), len(grid[0]), 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    cpar = 4
                    if row > 0 and grid[row-1][col] == 1: # check up
                        cpar -= 1
                    if row < rows-1 and grid[row+1][col] == 1: # check down
                        cpar -= 1
                    if col > 0 and grid[row][col-1] == 1: # check left
                        cpar -= 1
                    if col < cols-1 and grid[row][col+1] == 1: # check right
                        cpar -= 1
                    par += cpar
        return par
                    