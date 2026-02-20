class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN = -2 ** 31
        MAX = (2 ** 31) - 1

        sign = -1 if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else 1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1: return max(min(sign * dividend, MAX), MIN)
        if divisor == dividend: return sign

        ans = 0

        print(dividend, divisor)

        while dividend >= divisor:
            power = 0
            num = divisor
            print('start', dividend, divisor, num)
            while (num << 1) <= dividend:
                print('nested', dividend, num)
                power += 1
                num = num << 1
            print('end', dividend, num, power)
            ans += (2 ** power)
            dividend -= num
            print('ended', dividend, num)
        
        return  max(min(sign * ans, MAX), MIN)