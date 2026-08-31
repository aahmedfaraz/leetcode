class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)

        res = []

        for i in range(n):
            price = prices[i]
            found = False
            for j in range(i+1, n):
                newprice = prices[j]
                if newprice <= price:
                    found = True
                    res.append(price - newprice)
                    break
            if not found:
                res.append(price)

        return res