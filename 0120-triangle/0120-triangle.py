class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle

        for row in range(len(triangle)-1, 0, -1): # 
            for col in range(len(triangle[row])-1):
                dp[row-1][col] += min(dp[row][col], dp[row][col+1])

        return dp[0][0]

# test