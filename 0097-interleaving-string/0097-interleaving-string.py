from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s3)
        q, r = len(s1), len(s2)

        if q + r != n:
            return False

        @lru_cache(None)
        def solve(i, a, b):
            if i == n:
                return a == q and b == r
            
            if a < q and s3[i] == s1[a] and b < r and s3[i] == s2[b]:
                return solve(i+1, a+1, b) or solve(i+1, a, b+1)
            if a < q and s3[i] == s1[a]:
                return solve(i+1, a+1, b)
            elif b < r and s3[i] == s2[b]:
                return solve(i+1, a, b+1)
            else:
                return False

        return solve(0, 0, 0)