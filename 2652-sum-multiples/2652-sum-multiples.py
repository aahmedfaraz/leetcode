class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def gauss(n, steps):
            if steps == 1:
                return (n * (n+1)) // 2
            return steps * gauss(n//steps, 1)
        
        res = gauss(n, 3) + gauss(n, 5) + gauss(n, 7)
        res -= (gauss(n, 15) + gauss(n, 35) + gauss(n, 21))
        res += gauss(n, 105)

        return res
        