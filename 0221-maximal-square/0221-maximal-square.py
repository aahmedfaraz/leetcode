class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols+1)] for _ in range(rows+1)]

        maxval = 0

        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                if matrix[row][col] != '0':
                    dp[row][col] = 1
                    dp[row][col] += min(dp[row+1][col], dp[row][col+1], dp[row+1][col+1])
                    maxval = max(maxval, dp[row][col])
        
        return maxval ** 2

# Time = O(rows x cols)
# Space = O(rows x cols)