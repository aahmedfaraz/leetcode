class Solution:
    def romanToInt(self, s: str) -> int:
        rate = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        n = len(s)
        num = rate[s[n-1]]

        if n == 1: return num
        
        for i in range(n-2, -1, -1):
            if rate[s[i]] >= rate[s[i+1]]:
                num += rate[s[i]]
            else:
                num -= rate[s[i]]
        return num