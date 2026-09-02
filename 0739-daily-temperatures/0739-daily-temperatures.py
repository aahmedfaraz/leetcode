class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        if n <= 1: return [0] * n

        days = [0] * n
        mono = []

        for i in range(n-1, -1, -1):
            temp = temperatures[i]

            # stablize stack
            while mono and mono[-1][0] <= temp:
                mono.pop()
            
            # now get ans
            days[i] = mono[-1][1] - i if mono else 0

            # now add himself
            mono.append((temp, i))
        
        return days