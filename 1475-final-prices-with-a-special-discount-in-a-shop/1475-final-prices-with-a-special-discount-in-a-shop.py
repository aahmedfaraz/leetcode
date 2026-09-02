class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        if n <= 1: return prices

        finalprices = [0] * n
        mono = []

        for i in range(n-1, -1, -1):
            price = prices[i]
            
            # first make stack stable
            while mono and mono[-1] > price:
                mono.pop()

            # then see the ans
            if mono:
                finalprices[i] = price - mono[-1]
            else:
                finalprices[i] = price
            
            # now add himself
            mono.append(price)
        
        return finalprices
            
