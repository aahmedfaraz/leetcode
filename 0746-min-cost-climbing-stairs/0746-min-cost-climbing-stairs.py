class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+3)
        for i in range(n, -1, -1):
            dp[i] = (0 if i == 0 else cost[i-1]) + min(dp[i+1], dp[i+2])
        return dp[0]
        # memo = {}
        # def dfs(i):
        #     # print(i, memo)
        #     if i in memo:
        #         return memo[i]
        #     if i >= len(cost):
        #         return 0
        #     step1 = dfs(i+1)
        #     step2 = dfs(i+2)
        #     val = (0 if i < 0 else cost[i]) + min(step1, step2)
        #     memo[i] = val
        #     return val
        # return dfs(-1)

        # dp[i]

        # dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        # n -> 0

        # for val in range(n+2, -1, -1)