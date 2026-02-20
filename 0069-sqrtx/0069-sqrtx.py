class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x

        # 82 -> 9

        # 1 * 1 = 1
        # 2 * 2 = 4
        # 3 * 3 = 9
        # 4 * 4 = 16
        # 5 * 5 = 25
        # 6 * 6 = 
        # 7 * 7
        # 8 * 8
        # 9 * 9 = 81
        # 10 * 10 = 100

        i = 1
        while (i * i) <= x:
            i += 1

        return i - 1
