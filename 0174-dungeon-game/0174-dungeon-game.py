INF = float('inf')

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])

        if not rows or not cols: return 0

        # create dp
        dp = [INF] * (cols + 1)
        dp[cols - 1] = 1
        dp[cols] = INF

        # fill dp
        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                need = min(dp[col], dp[col + 1]) - dungeon[row][col]
                dp[col] = max(1, need)
        
        return dp[0]

# Time = O(rows x cols)
# Space = O(cols)