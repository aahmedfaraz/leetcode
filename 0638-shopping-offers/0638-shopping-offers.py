class Solution:
    def shoppingOffers(self, price: list[int], special: list[list[int]], needs: list[int]) -> int:
        items = len(price)
        n = len(special)

        def bt(idx, bucket, cost):
            mincost = cost

            # buy items indiv
            for i in range(items):
                if bucket[i] < needs[i]:
                    mincost += ((needs[i]-bucket[i]) * price[i])

            # try all special offers   
            for i in range(idx, n):
                offer = special[i]
                valid = True
                tempbucket = bucket[:]
                for j in range(len(offer)-1):
                    if bucket[j] + offer[j] <= needs[j]:
                        tempbucket[j] += offer[j]
                    else:
                        valid = False
                        break
                if valid:
                    mincost = min(mincost, bt(i, tempbucket, cost + offer[-1]))

            return mincost

        return bt(0, [0]*items, 0)