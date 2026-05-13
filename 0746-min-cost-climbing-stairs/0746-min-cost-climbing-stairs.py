class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i):
            # print(i, memo)
            if i in memo:
                return memo[i]
            if i >= len(cost):
                return 0
            step1 = dfs(i+1)
            step2 = dfs(i+2)
            val = (0 if i < 0 else cost[i]) + min(step1, step2)
            memo[i] = val
            return val
        return dfs(-1)