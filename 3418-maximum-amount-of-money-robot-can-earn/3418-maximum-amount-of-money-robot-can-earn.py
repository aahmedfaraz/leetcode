from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        rows, cols = len(coins), len(coins[0])

        # dp[j][k] → current row
        dp = [[float('-inf')] * 3 for _ in range(cols)]

        # initialize bottom-right
        for k in range(3):
            if coins[rows-1][cols-1] < 0 and k > 0:
                dp[cols-1][k] = 0
            else:
                dp[cols-1][k] = coins[rows-1][cols-1]

        # fill last row
        for j in range(cols-2, -1, -1):
            new = [float('-inf')] * 3
            for k in range(3):
                val = coins[rows-1][j]

                # take
                take = val + dp[j+1][k]

                # neutralize
                neut = float('-inf')
                if val < 0 and k > 0:
                    neut = dp[j+1][k-1]

                new[k] = max(take, neut)
            dp[j] = new

        # fill rest
        for i in range(rows-2, -1, -1):
            new_row = [[float('-inf')] * 3 for _ in range(cols)]

            for j in range(cols-1, -1, -1):
                for k in range(3):
                    val = coins[i][j]

                    best = float('-inf')

                    # right
                    if j + 1 < cols:
                        best = max(best, val + new_row[j+1][k])
                        if val < 0 and k > 0:
                            best = max(best, new_row[j+1][k-1])

                    # down
                    if i + 1 < rows:
                        best = max(best, val + dp[j][k])
                        if val < 0 and k > 0:
                            best = max(best, dp[j][k-1])

                    new_row[j][k] = best

            dp = new_row

        return dp[0][2]