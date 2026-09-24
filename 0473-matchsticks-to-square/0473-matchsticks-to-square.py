class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        summ = sum(matchsticks)
        length = summ//4

        if (length) != (summ/4):
            return False
        
        sides = [0] * 4

        matchsticks.sort(reverse=True)

        def bt(i):
            if i == len(matchsticks):
                return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if bt(i+1):
                        return True
                    sides[j] -= matchsticks[i]

            return False

        return bt(0)