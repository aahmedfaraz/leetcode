class Solution:
    def uniquePathsWithObstacles(self, o: List[List[int]]) -> int:
        if o[0][0] == 1: return 0
        m, n = len(o), len(o[0])
        dp = [1] * n
        found = False
        for box in range(n):
            obs = o[0][box]
            if obs == 1:
                found = True
            if found:
                dp[box] = 0
        # print(dp)

        for row in range(1, m):
            for col in range(n):
                if o[row][col] == 1:
                    dp[col] = 0
                else:
                    if col > 0:
                        dp[col] = dp[col] + dp[col-1]
            # print(dp)

        return dp[n-1]