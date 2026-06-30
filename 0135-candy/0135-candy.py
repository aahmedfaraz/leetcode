class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n <= 1:
            return n

        candies = [1] * n

        for i in range(n):
            mv = ratings[i]
            if i == 0:
                rv = ratings[i+1]
                if rv < mv:
                    candies[i] = max(candies[i], candies[i+1] + 1)
            elif i == n-1:
                lv = ratings[i-1]
                if lv < mv:
                    candies[i] = max(candies[i], candies[i-1] + 1)
            else:
                lv = ratings[i-1]
                if lv < mv:
                    candies[i] = max(candies[i], candies[i-1] + 1)
                rv = ratings[i+1]
                if rv < mv:
                    candies[i] = max(candies[i], candies[i+1] + 1)

        for i in range(n-1, -1, -1):
            mv = ratings[i]
            if i == 0:
                rv = ratings[i+1]
                if rv < mv:
                    candies[i] = max(candies[i], candies[i+1] + 1)
            elif i == n-1:
                lv = ratings[i-1]
                if lv < mv:
                    candies[i] = max(candies[i], candies[i-1] + 1)
            else:
                lv = ratings[i-1]
                if lv < mv:
                    candies[i] = max(candies[i], candies[i-1] + 1)
                rv = ratings[i+1]
                if rv < mv:
                    candies[i] = max(candies[i], candies[i+1] + 1)
        
        return sum(candies)
