class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        if n == 1:
            return False
        if len(set(s)) == 1:
            return True
        factors = []

        for num in range(2, (n // 2)+1):
            if n % num == 0:
                factors.append(num)

        # print(factors)

        if not factors:
            return False

        for factor in factors:
            substring = s[0:factor]

            if s[0:factor*2] != (substring+substring):
                continue

            multiple = n // factor
            sstring = substring * multiple
            # print(factor, sstring)
            if sstring == s:
                return True

        return False