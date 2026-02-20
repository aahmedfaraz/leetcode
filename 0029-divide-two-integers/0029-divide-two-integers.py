class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # limits
        MIN = -2 ** 31
        MAX = (2 ** 31) - 1

        # normalize
        sign = -1 if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)

        # edge cases
        if divisor == 1: return max(min(sign * dividend, MAX), MIN)
        if divisor == dividend: return sign

        # bit manipulation
        ans = 0
        while dividend >= divisor:
            power = 0
            num = divisor
            while (num << 1) <= dividend:
                power += 1
                num = num << 1
            ans += (2 ** power)
            dividend -= num
        
        return  max(min(sign * ans, MAX), MIN)