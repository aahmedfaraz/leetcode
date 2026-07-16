class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [0 for _ in range(cols+1)]

        maxval = 0

        for row in range(rows-1, -1, -1):
            diagonal = 0
            for col in range(cols-1, -1, -1):
                down = dp[col]
                right = dp[col+1]
                if matrix[row][col] == '1':
                    dp[col] = 1 + min(down, right, diagonal)
                    maxval = max(maxval, dp[col])
                else:
                    dp[col] = 0
                diagonal = down
        
        return maxval ** 2

# Time = O(rows x cols)
# Space = O(cols)