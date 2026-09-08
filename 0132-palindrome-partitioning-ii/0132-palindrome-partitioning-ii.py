from functools import lru_cache

class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n == 1: return 0

        dp = [([0] * n) for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1
        
        for start in range(1, n):
            row, col = 0, start
            # print("Start", start, "-", row, col)
            while col < n:
                mid = dp[row+1][col-1] if row+1 < col-1 else 1
                # print("\tprocess", row, col, mid)
                if mid == 0:
                    dp[row][col] = 0
                else:
                    dp[row][col] = 1 if s[row] == s[col] else 0
                row += 1
                col += 1

        @lru_cache(maxsize=None)
        def dfs(i):
            if i == n:
                return -1
            cuts = float('inf')
            for j in range(i, n):
                if dp[i][j] == 1:
                    cuts = min(cuts, 1 + dfs(j+1))
            return cuts
        
        return dfs(0)