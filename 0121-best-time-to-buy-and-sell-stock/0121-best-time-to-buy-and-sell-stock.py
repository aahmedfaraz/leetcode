class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minval, maxval, profit = float('inf'), float('-inf'), float('-inf')
        for num in prices:
            if num <= minval:
                minval = num
                maxval = -1
            elif num > maxval:
                maxval = num
                profit = max(profit, maxval - minval)

        return 0 if profit == float('-inf') else profit