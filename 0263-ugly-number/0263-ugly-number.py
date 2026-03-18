class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0: return False
        n = abs(n)
        f = 2
        while n > 1:
            if ((n / f) % 1) == 0:
                n /= f
            else:
                if f == 2:
                    f = 3
                elif f == 3:
                    f = 5
                else:
                    return False
        return n == 1