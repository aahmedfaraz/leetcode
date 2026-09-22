class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1

        ans = 10
        start = 9
        mul = 9

        for i in range(2, n+1):
            ans += start * mul
            start *= mul
            mul -= 1

        return ans