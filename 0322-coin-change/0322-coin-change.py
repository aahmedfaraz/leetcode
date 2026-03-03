class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1): # runs n times
            for coin in coins: # runs m times
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]

# Time = O(n x m)
# Space = O(n+1) size of dp list so, O(n)
# Where n = amount, m = no. of coins