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
        # dividend = 20
        while dividend >= divisor: # 20 | 10 | 4 ... divisor
            print('div', dividend)
            power = 0
            num = divisor
            while (num << 1) <= dividend: # num is doubled, loop runs O(log n) - 3 | 6 | ... dividend
                print("num", num)
                power += 1
                num = num << 1
            ans += (2 ** power)
            dividend -= num
        
        return  max(min(sign * ans, MAX), MIN)

# time complexity
# N = dividend
# - Outer loop - O(log N)
# - Inner loop - O(log N)
# Seems - O((log N)^2)
# Actual - O(log N) - because dividend shrinks exponentially each outer layer

# space complexity
# O(1)