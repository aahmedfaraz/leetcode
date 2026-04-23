class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n-1):
            if s[i] == '0':
                if s[i+1] == '1':
                    a, b = i, i+1
                    while a >= 0 and b < n and s[a] == '0' and s[b] == '1':
                        count += 1
                        a -= 1
                        b += 1

            else:
                if s[i+1] == '0':
                    a, b = i, i+1
                    while a >= 0 and b < n and s[a] == '1' and s[b] == '0':
                        count += 1
                        a -= 1
                        b += 1
        return count