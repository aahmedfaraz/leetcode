from functools import lru_cache

class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        items = len(price)
        n = len(special)

        @lru_cache(None)
        def bt(remaining):
            mincost = 0

            # buy items indiv
            for i in range(items):
                if remaining[i] > 0:
                    mincost += (remaining[i] * price[i])

            # try all special offers
            for offer in special:
                valid = True
                tempremaining = list(remaining)
                for j in range(len(offer)-1):
                    if (tempremaining[j] - offer[j]) >= 0:
                        tempremaining[j] -= offer[j]
                    else:
                        valid = False
                        break
                if valid:
                    mincost = min(mincost, offer[-1] + bt(tuple(tempremaining)))

            return mincost

        return bt(tuple(needs))