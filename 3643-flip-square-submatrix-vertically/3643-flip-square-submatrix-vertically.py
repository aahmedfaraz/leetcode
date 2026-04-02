class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for row in range(x, x+k // 2):
            secondRow = (x + k) - (row - x) - 1
            grid[row][y:y+k], grid[secondRow][y:y+k] = grid[secondRow][y:y+k], grid[row][y:y+k]
        return grid