class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = {}
        max1sinarea = 0

        def helper(row, col):
            nonlocal max1sinarea
            if row >= rows or col >= cols:
                return 0
            if (row, col) in cache:
                return cache[(row, col)]
            
            down = helper(row+1, col)
            right = helper(row, col+1)
            diag = helper(row+1, col+1)

            area = 0
            if matrix[row][col] == '1':
                area = 1 + min(down, right, diag)
                max1sinarea = max(max1sinarea, area ** 2)
                
            cache[(row, col)] = area
            return area
        
        helper(0, 0)
        return max1sinarea
# Time = O(rows x cols) = O(n)
# Space = O(rows x cols) = O(n)
