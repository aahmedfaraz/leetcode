class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        next1 = 0
        next2 = 0
        for i in range(n-1, -2, -1):       
            temp = next1
            next1 = (0 if i<0 else cost[i]) + min(next1, next2)
            next2 = temp   

        return next1