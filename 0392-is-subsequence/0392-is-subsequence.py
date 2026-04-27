class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, m = 0, len(s)
        j, n = 0 , len(t)

        while i < m and j < n:
            if t[j] == s[i]:
                i += 1
            j += 1
        
        return i == m