class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])

        INF = float('inf')

        dp = [INF] * (cols + 1)
        dp[cols - 1] = 1      # imaginary cell below princess
        dp[cols] = INF

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                need = min(dp[col], dp[col + 1]) - dungeon[row][col]
                dp[col] = max(1, need)

        return dp[0]