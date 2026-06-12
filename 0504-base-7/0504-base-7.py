class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = -1 if num < 0 else 1
        num = abs(num)
        ans = ""
        while num >= 7:
            ans += str(num % 7)
            num //= 7
        ans += str(num)
        if sign == -1:
            ans += "-"
        return ans[::-1]